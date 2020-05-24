from src.models import Movie, Genre
from src.app import db
import connexion

def read():
    all_movies = Movie.query.all()
    all_movies_dicts = [m.dump() for m in all_movies]
    return all_movies_dicts

def get_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie == None:
        return 'Movie not found', 404
    return movie.dump()

def add_movie(movie):
    movie_model = movie
    if connexion.request.is_json:
        movie_model = Movie.load(movie)

    db.session.add(movie_model)
    db.session.commit()

    return {}, 201

def replace_movie(movie_id, movie):
    movie_to_replace = Movie.query.filter_by(id=movie_id).one_or_none()
    movie['id'] = movie_id

    if movie_to_replace is not None:
        movie_to_replace.update(**movie)
    else:
        # Insert new movie
        movie_model = Movie.load(movie)
        db.session.add(movie_model)
    db.session.commit() # movie_to_replace ORM object is tracked => commit saves changes done to the object
