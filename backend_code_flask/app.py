
from flask import jsonify, request
from db_model import app, db, ma
from db_model.actor_model import Actor, ActorSchema, actor_schema, actors_schema
from db_model.film_model import Film, FilmSchema, film_schema, films_schema


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/actor/get', methods=['GET'])
def get_actors():
    print('call get actors')
    all_actors = Actor.query.all()
    results = actors_schema.dump(all_actors)
    print('result: ', results)
    return jsonify(results)

@app.route('/actor/get/<id>/', methods=['GET'])
def get_actor_by_id(id):
    actor = Actor.query.get(id)
    # results = actors_schema.dump(all_actors)
    return actor_schema.jsonify(actor)

@app.route('/actor/update/<id>/', methods=['PUT'])
def update_actor_by_id(id):
    actor = Actor.query.get(id)
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    # results = actors_schema.dump(all_actors)
    actor.first_name = first_name
    actor.last_name = last_name
    db.session.commit()
    return actor_schema.jsonify(actor)

@app.route('/actor/delete/<id>/', methods=['DELETE'])
def delete_actor_by_id(id):
    actor = Actor.query.get(id)
    db.session.delete(actor)
    db.session.commit()
    return actor_schema.jsonify(actor)

@app.route('/actor/add', methods=['POST'])
def add_actor():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    actor = Actor(first_name, last_name)
    db.session.add(actor)
    db.session.commit()
    return actor_schema.jsonify(actor)

##### film action API ########

@app.route('/film/get', methods=['GET'])
def get_films():
    print('call get films')
    all_films = Film.query.all()
    results = films_schema.dump(all_films)
    print('result: ', results)
    return jsonify(results)

@app.route('/film/get/<id>/', methods=['GET'])
def get_film_by_id(id):
    film = Film.query.get(id)
    # results = actors_schema.dump(all_actors)
    return film_schema.jsonify(film)

@app.route('/film/update/<id>/', methods=['PUT'])
def update_film_by_id(id):
    film = Film.query.get(id)
    title = request.json['title']
    description = request.json['description']
    release_year = request.json['release_year']
    # results = actors_schema.dump(all_actors)
    film.title = title
    film.description = description
    film.release_year = release_year
    db.session.commit()
    return film_schema.jsonify(film)

@app.route('/film/delete/<id>/', methods=['DELETE'])
def delete_film_by_id(id):
    film = Film.query.get(id)
    db.session.delete(film)
    db.session.commit()
    return film_schema.jsonify(film)

@app.route('/film/add', methods=['POST'])
def add_film():
    film_id = request.json['film_id']
    title = request.json['title']
    description = request.json['description']
    release_year = request.json['release_year']
    language_id = request.json['language_id']
    original_language_id = request.json['original_language_id']
    rental_duration = request.json['rental_duration']
    rental_rate = request.json['rental_rate']
    length = request.json['length']
    replacement_cost = request.json['replacement_cost']
    rating = request.json['rating']
    special_features = request.json['special_features']
    last_update = request.json['last_update']
    film = Film(film_id, title, description, release_year, language_id, original_language_id, \
                 rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update)
    db.session.add(film)
    db.session.commit()
    return actor_schema.jsonify(film)

if __name__ == '__main__':
    app.run()
