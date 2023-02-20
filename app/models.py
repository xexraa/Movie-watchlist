from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    
    cast: List[str] = field(default_factory=list)
    series: List[str] = field(default_factory=list)
    lastWatched: datetime = None
    rating: int = 0
    tags: List[str] = field(default_factory=list)
    description: str = None
    videoLink: str = None
    
    
@dataclass
class User:
    _id: str
    email: str
    password: str
    movies: List[str] = field(default_factory=list)