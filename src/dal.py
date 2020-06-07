from src.models import Movie, Genre
from src.app import db
import logging
from src.exceptions import NotFoundException
from pprint import pformat # To print dictinnaries with indentation

logger = logging.getLogger('data_access_layer')

def get_all_movies():
    all_movies = Movie.query.all()
    logger.info('Retrieved all movies from database.')
    return all_movies
    
def get_movie_by_id(movie_id):
    movie = Movie.query.get(movie_id)
    if movie == None:
        raise NotFoundException('Movie not found')
    logger.info(f'Movie with id : {movie_id} retrieved from database.')
    return movie

def add_movie_to_db(movie):
    movie_model = Movie.load(movie)
    db.session.add(movie_model)
    db.session.commit()
    logger.info(f'Added movie to database, movie info: {pformat(movie)}')

def replace_movie_in_db(movie_id, movie):
    movie_to_replace = Movie.query.filter_by(id=movie_id).one_or_none()
    movie['id'] = movie_id

    if movie_to_replace is not None:
        movie_to_replace.update(**movie)
        logger.info(f'Updated movie with id: {movie_id} in database.')
    else:
        # Insert new movie
        logger.info(f'Movie with id: {movie_id} to update is not found in database. inserting movie: {pformat(movie)}')

        movie_model = Movie.load(movie)
        db.session.add(movie_model)
    db.session.commit() # movie_to_replace ORM object is tracked => commit saves changes done to the object

def delete_movie_by_id(movie_id):
    movie_to_delete = Movie.query.filter_by(id=movie_id).one_or_none()
    if movie_to_delete is None:
        logger.info(f'Movie with id : {movie_id} to delete is not found in database.')
        raise NotFoundException('Movie not found')
    db.session.delete(movie_to_delete)
    db.session.commit()
    logger.info(f'Deleted movie with id: {movie_id} from database.')
    