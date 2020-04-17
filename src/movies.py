from src.models import Movie, Genre
from src.app import db

def read():
    all_movies = Movie.query.all()
    return all_movies

def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie == None:
        return 'Movie not found', 404
    return movie