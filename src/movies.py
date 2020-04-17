from src.models import Movie, Genre
from src.app import db

def read():
    all_movies = Movie.query.all()
    return all_movies

def get_movie(movie_id):
    return {}