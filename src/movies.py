from src.dal import get_all_movies, get_movie_by_id, add_movie_to_db, replace_movie_in_db, delete_movie_by_id
import logging
from src.exceptions import NotFoundException

logger = logging.getLogger('movies')

def read():
    logger.info('Read endpoit called!')
    try:
        all_movies_dicts = get_all_movies()
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500
    return all_movies_dicts

def get_movie(movie_id):
    logger.info('Get movie by id endpoit called!')
    try:
        movie = get_movie_by_id(movie_id)
    except NotFoundException as e:
        logger.exception(e)
        return 'Movie Not Found', 404
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500
    return movie.dump()

def add_movie(movie):
    logger.info('Add new movie endpoint called!')
    try:
        add_movie_to_db(movie)
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500
    return {}, 201

def replace_movie(movie_id, movie):
    logger.info('Replace movie endpoit called!')
    try:
        replace_movie_in_db(movie_id, movie)
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500

def delete_movie(movie_id):
    logger.info('Delete movie endpoit called!')
    try:
        delete_movie_by_id(movie_id)
    except NotFoundException as e:
        logger.exception(e)
        return 'Movie Not Found', 404
    except Exception as e:
        logger.exception(e)
        return 'Internal server error', 500