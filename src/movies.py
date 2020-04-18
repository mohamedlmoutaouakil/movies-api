from src.models import Movie, Genre
from src.app import db

def read():
    all_movies = Movie.query.all()
    all_movies_dicts = [m.dump() for m in all_movies]
    return all_movies_dicts

def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie == None:
        return 'Movie not found', 404
    return movie.dump()
