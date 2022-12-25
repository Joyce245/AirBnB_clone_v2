#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
import os
"""Test take a variable"""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def filters():
    """Start to show the filters dinamictly"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        citys = storage.all(City).values()
        cities = []
        for state_city in citys:
            for state in states:
                if state_city.state_id == state.id:
                    cities.append(state_city)
    else:
        cities = [[city for city in state.cities] for state in states]

    cities = sorted(cities, key=lambda k: k.name)
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def close(error):
    """Close the session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
