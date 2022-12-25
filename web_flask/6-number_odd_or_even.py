#!/usr/bin/python3
from flask import Flask, escape, render_template
"""Dinamyc html"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """return a str"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """return a str"""
    return 'HBNB'


@app.route('/c/<text>')
def TEXT(text):
    """return a str"""
    text = str(text).replace("_", " ")
    return 'C {}'.format(escape(text))


@app.route('/python/<text>')
@app.route('/python')
@app.route('/python/')
def is_cool(text='is cool'):
    """return a str"""
    text = str(text).replace("_", " ")
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>')
def integer(n):
    """return a str with a integer"""
    return '{} is a number'.format(escape(n))


@app.route('/number_template/<int:n>')
def int_template(n):
    """return a template with n"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """return a template with n and add a condition in the html"""
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
