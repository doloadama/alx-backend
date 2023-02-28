#!/usr/bin/env python3
"""0x02.i18n"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
@app.route("/", strict_slashes=False)
def index():
    """
    HANDLES / ROUTE
    """
    return render_template("0-index.html")
