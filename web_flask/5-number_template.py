#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB!"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays “C ” followed by the value of the text variable """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Displays “Python ” followed by the value of the text variable """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n' only if it is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
