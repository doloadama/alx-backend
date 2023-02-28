#!/usr/bin/env python3
"""
Get locale from request
"""
import babel
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config configuration class
    """
    LANGUAGES =  ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    The home/index page
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)

app.route("/",strict_slashes=False)
def index():
    """Hello World !!!
    """
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
