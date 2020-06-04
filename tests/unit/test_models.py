import pytest
from src.models import Genre, Movie
from tests.data_examples import movie_dict_example_1, genre_dict_example

def test_genre_load():
    # ARRANGE
    # ACT
    genre_model = Genre.load(genre_dict_example)

    # ASSERT
    assert genre_model.name == genre_dict_example.get('name')
