from datetime import datetime
from db_model import db
from db_model import ma

class Language(db.Model):
    language_id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String(20))
    last_update = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, lang_id, name, last_update):
        self.language_id = lang_id
        self.name = name
        self.last_update = last_update

    def __repr__(self):
        return '<Language {}>'.format(self.name)

class LanguageSchema(ma.Schema):
    class Meta:
        fields = ('lang_id','name','last_update')

lang_schema = LanguageSchema()
langs_schema = LanguageSchema(many=True)