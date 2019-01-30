import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

films = [
    {'id': 0,
     'title': 'Pulp Fiction',
     'director': 'Quentin Tarantino',
     'year': '1994'},
    {'id': 1,
     'title': 'Die Hard 3',
     'director': 'John McTiernan',
     'year': '1995'},
    {'id': 2,
     'title': 'Jurassic Park',
     'director': 'Steven Spielberg',
     'year': '1993'}
]



@app.route('/', methods=['GET'])
def home():
    return "<h1>Mi app de Pelis</h1><p>Este es mi sitio web super molón de películas de los 90.</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/films/all', methods=['GET'])
def api_all():
    return jsonify(films)

@app.route('/api/films', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for film in films:
        if film['id'] == id:
            results.append(film)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()