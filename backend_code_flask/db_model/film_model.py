from datetime import datetime
from db_model import db
from db_model import ma

class Film(db.Model):
    film_id = db.Column(db.INT,primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.TEXT)
    release_year = db.Column(db.INT)
    language_id = db.Column(db.INT)
    original_language_id = db.Column(db.INT)
    rental_duration = db.Column(db.INT)
    rental_rate = db.Column(db.FLOAT)
    length = db.Column(db.INT)
    replacement_cost = db.Column(db.FLOAT)
    rating = db.Column(db.String(5))
    special_features = db.Column(db.String(25))
    last_update = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, film_id, title, description, release_year, language_id, original_language_id, \
                 rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update):
        self.film_id = film_id
        self.title = title
        self.description = description
        self.release_year = release_year
        self.language_id = language_id
        self.original_language_id = original_language_id
        self.rental_duration = rental_duration
        self.rental_rate = rental_rate
        self.length = length
        self.replacement_cost = replacement_cost
        self.rating = rating
        self.special_features = special_features
        self.last_update = last_update

    def __repr__(self):
        return '<Film {}>'.format(self.title)

class FilmSchema(ma.Schema):
    class Meta:
        fields = ('film_id','title','description','release_year', 'language_id', \
                  'original_language_id', 'rental_duration', 'rental_rate', 'length' \
                  'replacement_cost', 'rating', 'special_features', 'last_update')

class FilmDetail(ma.Schema):
    class Meta:
        fields = ('film_id', 'title', 'description', 'release_year', 'language', 'length', 'rating', 'price')

film_schema = FilmSchema()
films_schema = FilmSchema(many=True)
film_detail_schema = FilmDetail()
films_detail_schema = FilmDetail(many=True)