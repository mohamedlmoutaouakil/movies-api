from src.app import db

movie_genre_table = db.Table('movie_genre', db.Model.metadata,
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'))
)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    poster = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.relationship('Genre', secondary=movie_genre_table)
    director = db.Column(db.String(50), nullable=True)

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)