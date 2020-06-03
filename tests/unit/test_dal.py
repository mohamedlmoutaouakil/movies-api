import pytest
from src.dal import get_all_movies, get_movie_by_id, add_movie_to_db, replace_movie_in_db
from src.models import Movie, Genre
from src.app import db

movie_dict_example_1 = {
    "description": "Description1",
    "director": "Director1",
    "duration": 100,
    "genre": [
      {
        "id": 1,
        "name": "Action"
      }
    ],
    "id": 1,
    "name": "Movie Example 1",
    "poster": "Poster URL 1",
    "rating": 7.0,
    "year": 2019
  }

movie_dict_example_2 = {
    "description": "Description2",
    "director": "Director2",
    "duration": 120,
    "genre": [
      {
        "id": 1,
        "name": "Action"
      }
    ],
    "id": 2,
    "name": "Movie Example 2",
    "poster": "Poster URL 2",
    "rating": 8.0,
    "year": 2020
  }



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
    assert all_movies[0] == movie_dict_example_1

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
    movie_dict_example_2['id'] = 1

    # ASSERT
    assert len(all_movies) == 1
    assert all_movies[0].dump() == movie_dict_example_2

def test_replace_movie_in_db_with_non_existing_id(setup_db):
    # ARRANGE
    # ACT
    replace_movie_in_db(2, movie_dict_example_2)
    # Retrieve the replaced movie
    all_movies = Movie.query.all()
    # Change movie_dict_example_2's id to 1 (id is autoincrement => first movie inserted will have id 1)
    movie_dict_example_2['id'] = 1

    # ASSERT
    assert len(all_movies) == 1
    assert all_movies[0].dump() == movie_dict_example_2