#!/usr/bin/python3
from flask import Flask
"""Put a second route"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Return a string"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """Another list"""
    return 'HBNB'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
