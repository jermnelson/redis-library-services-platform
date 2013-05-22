"""cluster module is a JSON interface to a RLSP Cluster


"""
__author__ = "Jeremy Nelson"
import json
import os
import sys

from bottle import request, route, run, static_file
from bottle import jinja2_view as view
from bottle import jinja2_template as template


@route("/")
def index():
    return template('index.html')




run(host='0.0.0.0', port=8042)
