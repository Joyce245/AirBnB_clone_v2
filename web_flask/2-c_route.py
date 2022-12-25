#!/usr/bin/python3
"""Flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """hello_route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """c_route"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
