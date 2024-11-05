#!/usr/bin/env python3
"""
Basic Hello world flask app
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Optional

class Config:
    """
    Configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyoncé", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Optional[Dict]:
    """
    Retrieve users
    """
    try:
        login_as = request.args.get('login_as')
        if login_as:
            user_id = int(login_as)
            return users.get(user_id)
    except (ValueError, TypeError):
        pass
    return None


@app.before_request
def before_request():
    """Preruns before every test"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Determine best match of a supported language"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Route for the index page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
