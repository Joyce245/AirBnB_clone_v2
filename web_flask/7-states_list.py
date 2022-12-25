#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage
from models.state import State
"""Test take a variable"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def state_list():
    """list of all State objects present in DBStorage"""
    list_states = [value for key, value in storage.all(State).items()]
    list_states = sorted(list_states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=list_states)


@app.teardown_appcontext
def close(error):
    """Close the session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
