import pytest
from src.models import Genre, Movie
from tests.data_examples import movie_dict_example_1, genre_dict_example, movie_model_example_1

def test_genre_load():
    # ARRANGE
    # ACT
    genre_model = Genre.load(genre_dict_example)

    # ASSERT
    assert genre_model.name == genre_dict_example.get('name')

# We added setup_db fixture because Movie.load queries the genre table
# So we need to connect to the database
def test_movie_load(setup_db):
    # ARRANGE
    # ACT
    movie_model = Movie.load(movie_dict_example_1)

    # ASSERT
    assert movie_model.name == movie_dict_example_1.get('name')
    assert movie_model.description == movie_dict_example_1.get('description')
    assert movie_model.duration == movie_dict_example_1.get('duration')
    assert movie_model.poster == movie_dict_example_1.get('poster')
    assert movie_model.rating == movie_dict_example_1.get('rating')
    assert movie_model.year == movie_dict_example_1.get('year')
    assert movie_model.director == movie_dict_example_1.get('director')
    assert movie_model.genre[0].id == None
    assert movie_model.genre[0].name == movie_dict_example_1.get('genre')[0].get('name')

def test_genre_dump():
    # ARRANGE
    genre_model = Genre()
    genre_model.id = 1
    genre_model.name = 'Action'

    # ACT
    genre_dict = genre_model.dump()

    # ASSERT
    assert genre_dict == genre_dict_example

def test_movie_dump():
    # ARRANGE    
    # ACT
    movie_dict = movie_model_example_1.dump()

    # ASSERT
    assert movie_dict == movie_dict_example_1