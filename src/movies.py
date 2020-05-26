from src.models import Movie, Genre
from src.app import db
import connexion
import logging

logger = logging.getLogger('movies')

def read():
    logger.info('Read endpoit called!')
    try:
        all_movies = Movie.query.all()
        all_movies_dicts = [m.dump() for m in all_movies]
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500
    logger.info('Retrieved all movies from database.')
    return all_movies_dicts

def get_movie(movie_id):
    logger.info('Get movie by id endpoit called!')
    try:
        movie = Movie.query.get(movie_id)
        if movie == None:
            logger.info(f'Movie with id : {movie_id} to retrieve is not found in database.')
            return 'Movie not found', 404
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500
    logger.info(f'Movie with id : {movie_id} retrieved from database.')
    return movie.dump()

def add_movie(movie):
    movie_model = movie
    try:
        if connexion.request.is_json:
            movie_model = Movie.load(movie)

        db.session.add(movie_model)
        db.session.commit()
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500
    logger.info(f'Added movie to database, movie info: {movie}')

    return {}, 201

def replace_movie(movie_id, movie):
    try:
        movie_to_replace = Movie.query.filter_by(id=movie_id).one_or_none()
        movie['id'] = movie_id

        if movie_to_replace is not None:
            movie_to_replace.update(**movie)
            logger.info(f'Updated movie with id: {movie_id} in database.')
        else:
            # Insert new movie
            logger.info(f'Movie with id: {movie_id} to update is not found in database. inserting movie: {movie}.')
            movie_model = Movie.load(movie)
            db.session.add(movie_model)
        db.session.commit() # movie_to_replace ORM object is tracked => commit saves changes done to the object
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500

def delete_movie(movie_id):
    try:
        movie_to_delete = Movie.query.filter_by(id=movie_id).one_or_none()
        
        if movie_to_delete is None:
            logger.info(f'Movie with id : {movie_id} to delete is not found in database.')
            return 'Movie not found', 404
        db.session.delete(movie_to_delete)
        db.session.commit()
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500
    logger.info(f'Deleted movie with id: {movie_id} from database.')