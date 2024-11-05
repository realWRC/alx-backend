#!/usr/bin/env python3
"""
Basic Hello world flask app
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Route for the index page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
