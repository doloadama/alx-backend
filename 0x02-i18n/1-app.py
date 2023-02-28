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
Babel = Babel(app)
app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def index():
    """
    HANDLES / ROUTE
    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(debug=True)
