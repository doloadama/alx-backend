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
    return render_template("index.html")

class Config:
    """
    has a language class attribute
    """
    LANGUAGES = ["en", "fr"]

babel = Babel(app, locals=Config.LANGUAGES, timezone_selector="UTC")
app.config.from_object(Config)
