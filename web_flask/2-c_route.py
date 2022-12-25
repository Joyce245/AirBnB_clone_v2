#!/usr/bin/python3
from flask import Flask, escape
"""Test take a variable"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Return a list"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """Another return of a list with another woute"""
    return 'HBNB'


@app.route('/c/<text>')
def TEXT(text):
    """Display a prompo with the url"""
    text = str(text).replace("_", " ")
    return 'C {}'.format(escape(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
