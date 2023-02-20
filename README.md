# Movie Watchlist

## Web project.

This is a site for creating a watchlist of videos added by users

## Where to start?
The application has a home page, a login and registration section, a light and dark mode, after logging in a list of videos that the user has added.
1. Home page with dark and light mode
     ![wlistblack](https://user-images.githubusercontent.com/121942715/220152869-4f0f3bc4-9821-4f97-ba07-cb91d05d3985.png)
     ![wlistwhite](https://user-images.githubusercontent.com/121942715/220152820-abb5093c-2857-4e03-aebc-a325b45f207b.png)
2. Login and registration section
     ![login](https://user-images.githubusercontent.com/121942715/220154773-c04f3375-ee63-4ce7-90df-e27c06bbce59.png)
     ![register](https://user-images.githubusercontent.com/121942715/220154834-2bd2ea5d-2f88-4280-862f-215704e38403.png)
3. When the user has no movie added
     ![beforeadd](https://user-images.githubusercontent.com/121942715/220155255-e44ab0b4-46e2-4f87-8838-6c8017e22630.png)
4. After pressing "Add one here!" or the lower "+" button, we enter the add movie section which has 3 mandatory fields:
     ![newmovie](https://user-images.githubusercontent.com/121942715/220155886-eb30fb11-41e7-48a5-af86-3f973172d08c.png)
5. After adding one, we are redirected to that movie's page
     ![movie](https://user-images.githubusercontent.com/121942715/220159756-f48ba28c-76b6-46dc-89f9-1b66fcc9a203.png)
    In movie section:
    - we can add starts from 1 to 5, default is 0
    - we can mark when we watched this movie by pressing the "Not watched yet" link or "Last watched" link to update for today's day
    - finally we can enter the edit section to add more details of this movie
6. Edit section has some additional fields that are not required by default
    ![edit](https://user-images.githubusercontent.com/121942715/220161664-eb3038a6-eb14-446a-8fa3-388ce0ea55b1.png)
   - if there are already any data that the user has added, they will be written in its field by default
   - submit button will save the changes we want to make
   - delete button allows you to delete the video, but before we do it, we will be redirected to the next page to confirm our action
7. After pressing the "Delete" button
     ![delete](https://user-images.githubusercontent.com/121942715/220162901-f9e74b7e-c3bd-4160-9072-06d5f2e07bd2.png)
8. After deletion, we will receive a confirmation in the form of a flash message
     ![afterdelete](https://user-images.githubusercontent.com/121942715/220163091-6640eece-3737-4ffd-9147-b102bc3e0f59.png)
9. Each user has his own list of movies that he has added, other users do not have access to it
     ![user1](https://user-images.githubusercontent.com/121942715/220163594-d5d87845-54b2-43c7-b400-567828b9e928.png)
     ![user2](https://user-images.githubusercontent.com/121942715/220163621-e9642541-e76e-4dd2-8246-3692b357b125.png)

## In short

- the main page is open to the public and has a list of all videos that have been added by users
- after logging in, everyone has access to their private movie list
- deletion and editing is done only by logged in users and only in your own movie list
- there is an option to track when I last watched this video by clicking on the link and rate it by adding stars
- and there is a publicly available option that does not require logging in to set a light or dark mode

## What sources did I use?

**Python:**

- flask
- flask-wtf
- flask-security
- python-dotenv
- pymongo
- email_validator
- passlib
- gunicorn (needed mainly to place a page on render.com)


**Programs:**

- MongoDBCompass
- GIT
- VSC

**Pages that were helpful:**

- render.com
- cloud.mongodb.com
