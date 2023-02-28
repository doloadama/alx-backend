#!/usr/bin/env python3
"""3.Parametrize templates"""
from flask import Flask,  render_template, request
from flask_babel import Babel, gettext



app = Flask(__name__)
Babel = Babel(app)


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    """
     determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index():
    return render_template("3-index.html")

if __name__ == '__main__':
    app.run(debug=True)
