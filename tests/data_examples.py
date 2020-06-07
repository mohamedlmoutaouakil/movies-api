from src.models import Movie, Genre

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

genre_dict_example = {
    'id': 1,
    'name': 'Action'
}

# Movie model examples

movie_model_example_1 = Movie()
movie_model_example_1.id = 1
movie_model_example_1.name = 'Movie Example 1'
movie_model_example_1.description = 'Description1'
movie_model_example_1.duration = 100
movie_model_example_1.poster = 'Poster URL 1'
movie_model_example_1.rating = 7.0
movie_model_example_1.year = 2019
# Instanciate a genre model example
genre_model = Genre()
genre_model.id = 1
genre_model.name = 'Action'
# Append genre example to genre list in movie model
movie_model_example_1.genre.append(genre_model)
movie_model_example_1.director = 'Director1'