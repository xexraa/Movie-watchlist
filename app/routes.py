import uuid
import datetime
import functools
from flask import Blueprint, render_template, session, redirect, request, current_app, url_for, flash
from dataclasses import asdict
from app.forms import MovieForm, ExtendedMovieForm, RegisterForm, LoginForm
from app.models import Movie, User
from passlib.hash import pbkdf2_sha256


blp = Blueprint("pages", __name__, template_folder="templates", static_folder="static")


def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args, **kwargs):
        if session.get("email") is None:
            return redirect(url_for(".login"))
        return route(*args, **kwargs)
    return route_wrapper

@blp.route("/")
def all_movie():
    movieList = [movie for movie in current_app.db.movie.find({})]
    return render_template("all_movie.html", title="List of movies", movie_list=movieList)

@blp.route("/home")
@login_required
def index():
    userData = current_app.db.user.find_one({"email": session["email"]})
    user = User(**userData)
    
    movieData = current_app.db.movie.find({"_id": {"$in": user.movies}})
    movies = [Movie(**movie) for movie in movieData]
    
    return render_template("index.html", title="Movies Watchlist", movies_data=movies)


@blp.route("/register", methods=["GET", "POST"])
def register():
    if session.get("email"):
        return redirect(url_for(".index"))
    
    form = RegisterForm()
    
    if form.validate_on_submit():
        user = User(_id=uuid.uuid4().hex, email=form.email.data, password=pbkdf2_sha256.hash(form.password.data))   
        current_app.db.user.insert_one(asdict(user))
        flash("User registered successfully", "success")       
        return redirect(url_for(".login"))
    
    return render_template("register.html", title="Movies Watchlist - Register", form=form)


@blp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("email"):
        return redirect(url_for(".index"))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        userData = current_app.db.user.find_one({"email": form.email.data})
        if not userData:
            flash("Login credentials not correct", category="danger")
            return redirect(url_for(".login"))
        user = User(**userData)
        
        if user and pbkdf2_sha256.verify(form.password.data, user.password):
            session["user_id"] = user._id
            session["email"] = user.email
            
            return redirect(url_for(".index"))
        
        flash("Login credentials not correct", category="danger")
        
    return render_template("login.html", title="Movie Watchlist - Login", form=form)


@blp.route("/logout")
def logout():
    currentTheme = session.get("theme")
    session.clear() 
    session["theme"] = currentTheme
    
    return redirect(url_for(".login"))


@blp.route("/add", methods=["GET", "POST"])
@login_required
def add_movie():
    form = MovieForm()
    
    if form.validate_on_submit():
        movie = Movie(_id=uuid.uuid4().hex, title=form.title.data, director=form.director.data, year=form.year.data)
        
        current_app.db.movie.insert_one(asdict(movie))
        current_app.db.user.update_one({"_id": session["user_id"]}, {"$push": {"movies": movie._id}})
        
        return redirect(url_for(".movie", _id=movie._id))
    
    return render_template("new_movie.html", title="Movies Watchlist - Add Movie", form=form)


@blp.route("/edit/<string:_id>", methods=["GET", "POST"])
@login_required
def edit_movie(_id: str):
    movie = Movie(**current_app.db.movie.find_one({"_id": _id}))
    form = ExtendedMovieForm(obj=movie)
    if form.validate_on_submit():      
        movie.title = form.title.data
        movie.description = form.description.data
        movie.year = form.year.data
        movie.cast = form.cast.data
        movie.series = form.series.data
        movie.tags = form.tags.data
        movie.videoLink = form.videoLink.data
                
        current_app.db.movie.update_one({"_id": movie._id}, {"$set": asdict(movie)})
        return redirect(url_for(".movie", _id=movie._id))
       
    return render_template("movie_form.html", movie=movie, form=form)


@blp.route("/delete/<string:_id>", methods=["GET", "POST"])
@login_required
def delete(_id: str):
    movie = Movie(**current_app.db.movie.find_one({"_id": _id}))
    form = ExtendedMovieForm(obj=movie)
    if form.validate_on_submit():
        if form.delete.data:
            current_app.db.movie.delete_one({"_id": movie._id})
            flash("The video was deleted successfully.", "success") 
            return redirect(url_for('.index'))
    
    return render_template("confirmation.html", form=form)
    

@blp.get("/movie/<string:_id>")
def movie(_id: str):
    movie = Movie(**current_app.db.movie.find_one({"_id": _id}))
    return render_template("movie_details.html", movie=movie)


@blp.get("/movie/<string:_id>/rate")
@login_required
def rate_movie(_id):
    rating = int(request.args.get("rating"))
    current_app.db.movie.update_one({"_id": _id}, {"$set": {"rating": rating}})
    
    return redirect(url_for('.movie', _id=_id))


@blp.get("/movie/<string:_id>/watch")
@login_required
def movie_watch_today(_id):
    current_app.db.movie.update_one({"_id": _id}, {"$set": {"lastWatched": datetime.datetime.today()}})
    
    return redirect(url_for('.movie', _id=_id))

@blp.get("/toggle-theme")
def toggle_theme():
    currentTheme = session.get("theme")
    if currentTheme == 'dark':
        session['theme'] = 'light'
    else:
        session['theme'] = 'dark'
    return redirect(request.args.get("current_page")) 