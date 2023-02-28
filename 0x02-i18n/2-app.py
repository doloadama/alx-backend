#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel
import babel


class Config(object):
    """
    Config configuration class
    """
    LANGUAGES =  ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    The home/index page
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.route("/",strict_slashes=False)
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
