import enum
from datetime import datetime
from db_model import db
from db_model import ma

class Actor(db.Model):
    actor_id = db.Column(db.INT,primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    last_update = db.Column(db.DateTime, default=datetime.now())

    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<Actor {}>'.format(self.first_name+' '+self.last_name)

class RatingEnum(enum.Enum):
    first = 'G'
    second = 'PG'
    third = 'PG-13'
    fourth = 'R'
    fifth = 'NC-17'

class ActorSchema(ma.Schema):
    class Meta:
        fields = ('actor_id','first_name','last_name','last_update')

actor_schema = ActorSchema()
actors_schema = ActorSchema(many=True)


