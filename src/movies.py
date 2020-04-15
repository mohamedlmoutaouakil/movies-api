
movies_list = [
    {
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
    }
]

def read():
    return movies_list