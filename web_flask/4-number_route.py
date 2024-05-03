#!/usr/bin/python3
"""Flask web application startd"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """'Hello HBNB!' displayd"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """'HBNB' displayd"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """'C' displayd followed by the value of <text>.
    """
    txt = text.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """'Python' displayd followed by the value of <text>.
    """
    txt = text.replace("_", " ")
    return "Python {}".format(txt)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """'n is a number' displayd only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
