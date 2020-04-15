
movies_list = {
    1: {
        "id": 1,
        "name": 'Fight Club',
        "description": 'An office worker meets a soap maker and started an underground fight club.',
        "duration": 118,
        "poster": "https://mypostercollection.com/wp-content/uploads/2018/07/Fight-Club-MyPosterCollection.com-1-683x1024.jpg",
        "rating": 8.8,
        "year": 1999,
        "genre": 
            [
                {
                    "id": 1,
                    "name": 'Action'
                },
                {
                    "id": 2,
                    "name": 'Drama'
                }
            ],
        "director": 'David Fincher'
    },
    2: {
        "id": 2,
        "name": 'The Equalizer',
        "description": 'McCall gives up violence and wishes to lead a quiet and undisturbed life. However, brutal events force him to once again take up the fight for justice.',
        "duration": 132,
        "poster": "https://www.movienewsletters.net/photos/140326R1.jpg",
        "rating": 7.2,
        "year": 2014,
        "genre": 
            [
                {
                    "id": 1,
                    "name": 'Action'
                },
                {
                    "id": 3,
                    "name": 'Thriller'
                }
            ],
        "director": 'Antoine Fuqua'
    }
}

def read():
    return movies_list.values()

def get_movie(movie_id):
    if movie_id in movies_list.keys():
        return movies_list[movie_id]