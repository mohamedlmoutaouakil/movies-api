import pytest
from tests.data_examples import movie_dict_example_1, movie_dict_example_2
from src.app import db
from src.models import Movie, Genre

def test_read(test_client):
    # ARRANGE
    # Insert a movie in database
    movie_model = Movie.load(movie_dict_example_1)
    db.session.add(movie_model)
    db.session.commit()

    # ACT
    response = test_client.get('/movies')
    all_movies = response.json

    # ASSERT
    assert response.status_code == 200
    assert len(all_movies) == 1
    assert all_movies[0] == movie_dict_example_1
