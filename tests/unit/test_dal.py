import pytest
from src.dal import get_all_movies, get_movie_by_id, add_movie_to_db, replace_movie_in_db, delete_movie_by_id
from src.models import Movie, Genre
from src.app import db
from src.exceptions import NotFoundException
from tests.data_examples import movie_dict_example_1, movie_dict_example_2

def test_get_all_movies(setup_db):
    # ARRANGE
    # Insert a movie in database
    movie_model = Movie.load(movie_dict_example_1)
    db.session.add(movie_model)
    db.session.commit()

    # ACT
    all_movies = get_all_movies()

    # ASSERT
    assert len(all_movies) == 1
    assert all_movies[0].dump() == movie_dict_example_1

def test_get_movie_by_id(setup_db):
    # ARRANGE
    # Insert movies in db
    movie_model_1 = Movie.load(movie_dict_example_1)
    db.session.add(movie_model_1)
    db.session.commit() # So we can re-use the Genre model inserted above
    movie_model_2 = Movie.load(movie_dict_example_2) # Instead of inserting new Genre we retrieve the one above from db
    db.session.add(movie_model_2)
    db.session.commit()

    # ACT
    movie1 = get_movie_by_id(1)
    movie2 = get_movie_by_id(2)

    # ASSERT
    assert movie1.dump() == movie_dict_example_1
    assert movie2.dump() == movie_dict_example_2

def test_get_movie_by_id_with_non_existing_id(setup_db):
    # ARRANGE
    # ACT
    # ASSERT
    with pytest.raises(NotFoundException) as e:
        get_movie_by_id(1)

def test_add_movie_to_db(setup_db):
    # ARRANGE
    add_movie_to_db(movie_dict_example_1)

    # ACT
    all_movies = Movie.query.all()

    # ASSERT
    assert len(all_movies) == 1
    assert all_movies[0].dump() == movie_dict_example_1

def test_replace_movie_in_db_with_existing_id(setup_db):
    # ARRANGE
    # Insert a movie in database
    movie_model = Movie.load(movie_dict_example_1)
    db.session.add(movie_model)
    db.session.commit()

    # ACT
    replace_movie_in_db(1, movie_dict_example_2)
    # Retrieve the replaced movie
    all_movies = Movie.query.all()
    # Change movie_dict_example_2's id to 1 (id of movie to replace)
    movie_dict_example_2_copy = movie_dict_example_2.copy()
    movie_dict_example_2_copy['id'] = 1

    # ASSERT
    assert len(all_movies) == 1
    assert all_movies[0].dump() == movie_dict_example_2_copy

def test_replace_movie_in_db_with_non_existing_id(setup_db):
    # ARRANGE
    # ACT
    replace_movie_in_db(2, movie_dict_example_2)
    # Retrieve the replaced movie
    all_movies = Movie.query.all()
    # Change movie_dict_example_2's id to 1 (id is autoincrement => first movie inserted will have id 1)
    movie_dict_example_2_copy = movie_dict_example_2.copy()
    movie_dict_example_2_copy['id'] = 1

    # ASSERT
    assert len(all_movies) == 1
    assert all_movies[0].dump() == movie_dict_example_2_copy

def test_delete_movie_by_id(setup_db):
    # ARRANGE
    # Insert a movie in database
    movie_model = Movie.load(movie_dict_example_1)
    db.session.add(movie_model)
    db.session.commit()

    # ACT
    delete_movie_by_id(1)
    # Retrieve all movies
    all_movies = Movie.query.all()

    # ASSERT
    assert len(all_movies) == 0

def test_delete_movie_by_id_with_non_existing_id(setup_db):
    # ARRANGE
    # ACT
    # ASSERT
    with pytest.raises(NotFoundException) as e:
        delete_movie_by_id(1)