#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
import os
"""Test take a variable"""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def filters_and_places():
    """Show dinamictly"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    users = storage.all(User).values()
    users = sorted(users, key=lambda k: k.first_name)

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
    return render_template('100-hbnb.html', states=states,
                           cities=cities, amenities=amenities,
                           places=places, users=users)


@app.teardown_appcontext
def close(error):
    """Close the session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
