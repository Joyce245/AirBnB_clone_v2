#!/usr/bin/python3
from flask import Flask, escape
"""Put a default value in a varible"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Return a str"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """Return str"""
    return 'HBNB'


@app.route('/c/<text>')
def TEXT(text):
    """Return str"""
    text = str(text).replace("_", " ")
    return 'C {}'.format(escape(text))


@app.route('/python/<text>')
@app.route('/python')
@app.route('/python/')
def is_cool(text='is cool'):
    """Put difetrent routes"""
    text = str(text).replace("_", " ")
    return 'Python {}'.format(escape(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
