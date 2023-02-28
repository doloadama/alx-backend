#!/usr/bin/env python3
"""0x02.i18n"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
@app.route("/")
def index():
    """
    HANDLES / ROUTE
    """
    return render_template("1-index.html")


class Config:
    """
    Config class
    """
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
