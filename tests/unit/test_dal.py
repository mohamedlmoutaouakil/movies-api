import pytest
from src.dal import get_all_movies
from src.models import Movie, Genre
from src.app import db

movie_dict_example = {
    "description": "Description",
    "director": "Director",
    "duration": 100,
    "genre": [
      {
        "id": 1,
        "name": "Action"
      }
    ],
    "id": 1,
    "name": "Movie Example",
    "poster": "Poster URL",
    "rating": 7.0,
    "year": 2020
  }



def test_get_all_movies(setup_db):
    # ARRANGE
    # Insert a movie in database
    movie_model = Movie.load(movie_dict_example)
    db.session.add(movie_model)
    db.session.commit()

    # ACT
    all_movies = get_all_movies()

    # ASSERT
    assert len(all_movies) == 1
    assert all_movies[0] == movie_dict_example
