#!/usr/bin/python3
"""Flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """hello_route"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
