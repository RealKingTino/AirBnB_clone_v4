#!/usr/bin/python3
"""
Starts a Flask web application.
"""

import uuid
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown.
    """
    storage.close()


@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """
    Fetches necessary data and renders the template.
    """
    cache_id = str(uuid.uuid4())

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    st_ct = []

    for state in sorted_states:
        sorted_cities = sorted(state.cities, key=lambda city: city.name)
        st_ct.append([state, sorted_cities])

    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)

    places = storage.all(Place).values()
    sorted_places = sorted(places, key=lambda place: place.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=sorted_amenities,
                           places=sorted_places,
                           cache_id=cache_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
