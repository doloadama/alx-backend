#!/usr/bin/env python3
"""0x02.i18n"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
Babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """
    HANDLES / ROUTE
    """
    return render_template("1-index.html")
