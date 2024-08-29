#!/usr/bin/env python3
"""app.py"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _, format_datetime
import pytz
from datetime import datetime

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    try:
        timezone = request.args.get('timezone')
        if timezone:
            return pytz.timezone(timezone).zone
        if g.user and g.user['timezone']:
            return pytz.timezone(g.user['timezone']).zone
        return app.config['BABEL_DEFAULT_TIMEZONE']
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def index():
    timezone = get_timezone()
    current_time = datetime.now(pytz.timezone(timezone))
    formatted_time = format_datetime(current_time, format="medium")
    return render_template('7-index.html', current_time=formatted_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
