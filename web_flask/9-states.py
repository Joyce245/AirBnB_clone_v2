#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.city import City
import os
"""Test take a variable"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def state_list():
    """list of all State objects present in DBStorage"""
    list_states = [value for key, value in storage.all(State).items()]
    list_states = sorted(list_states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=list_states)


@app.route('/cities_by_states')
def cities_by_states():
    """Print the states with each one og their cities"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        cities = storage.all(City).values()
    else:
        cities = [[city for city in state.cities] for state in states]

    cities = sorted(cities, key=lambda k: k.name)
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """Display all statates or the state with the id
    with his cities"""

    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)

    flag = 0

    if id is None:
        flag = 1

    for state in states:
        if state.id == id:
            id_state = state
            flag = 2
            break

    if flag == 1:

        return render_template('9-states.html', states=states, flag=flag)

    elif flag == 2:

        if os.getenv('HBNB_TYPE_STORAGE') == "db" and id_state:
            citys = storage.all(City).values()
            cities = [state_city for state_city in citys
                      if state_city.state_id == id_state.id]
        else:
            cities = [city for city in id_state.cities]

        cities = sorted(cities, key=lambda k: k.name)
        return render_template('9-states.html', state_id=id_state,
                               cities=cities, flag=flag)

    return render_template('9-states.html', flag=flag)


@app.teardown_appcontext
def close(error):
    """Close the session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
