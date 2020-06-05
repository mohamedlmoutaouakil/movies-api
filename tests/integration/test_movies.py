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

def test_get_movie_with_existing_id(test_client):
    # ARRANGE
    # Insert movies in db
    movie_model_1 = Movie.load(movie_dict_example_1)
    db.session.add(movie_model_1)
    db.session.commit() # So we can re-use the Genre model inserted above
    movie_model_2 = Movie.load(movie_dict_example_2) # Instead of inserting new Genre we retrieve the one above from db
    db.session.add(movie_model_2)
    db.session.commit()
    movie_id = 1

    # ACT
    response = test_client.get(f'/movies/{movie_id}')
    movie_dict = response.json

    # ASSERT
    assert response.status_code == 200
    assert movie_dict == movie_dict_example_1

def test_get_movie_with_non_existing_id(test_client):
    # ARRANGE
    movie_id = 1

    # ACT
    response = test_client.get(f'/movies/{movie_id}')

    # ASSERT
    assert response.status_code == 404
    assert response.json == 'Movie Not Found'
