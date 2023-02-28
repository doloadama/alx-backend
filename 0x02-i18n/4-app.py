#!/usr/bin/env python3
"""3.Parametrize templates"""
from flask import Flask,  render_template, request
from flask_babel import Babel
import babel


app = Flask(__name__)
babel = Babel(app)


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
    loc = request.args.get('locale')
    if loc:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index() -> str:
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run(debug=True)
