from src.app import db

movie_genre_table = db.Table('movie_genre', db.Model.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'))
)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    poster = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.relationship('Genre', secondary=movie_genre_table)
    director = db.Column(db.String(50), nullable=True)

    @classmethod
    def load(cls, movie_dict):
        movie_model = Movie(
            name=movie_dict.get('name'),
            description=movie_dict.get('description'),
            duration=movie_dict.get('duration'),
            poster=movie_dict.get('poster'),
            rating=movie_dict.get('rating'),
            year=movie_dict.get('year'),
            director=movie_dict.get('director')
        )
        # Retrieve the json list of Genres of the movie
        # If the genre already exists in database then append it to genres list of Movie model
        for genre_dict in movie_dict.get('genre'):
            genre_id = genre_dict.get('id')
            genre_in_db = Genre.query.get(genre_id)
            if genre_in_db == None:
            movie_model.genre.append(Genre.load(genre_dict))
            else:
                movie_model.genre.append(genre_in_db)
        return movie_model

    def dump(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'duration': self.duration,
            'poster': self.poster,
            'rating': self.rating,
            'year': self.year,
            'genre': [g.dump() for g in self.genre],
            'director': self.director
        }

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    @classmethod
    def load(cls, genre_dict):
        return Genre(
            name=genre_dict.get('name')
        )

    def dump(self):
        return {
            'id': self.id,
            'name': self.name
        }