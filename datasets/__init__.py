"""dataset module is a JSON interface to a RLSP Cluster


"""
__author__ = "Jeremy Nelson"
import json
import os
import sys

from bottle import request, route, run, static_file
from bottle import jinja2_view as view
from bottle import jinja2_template as template

PROJECT_ROOT = os.path.split(os.path.abspath(__name__))[0]


@route('/assets/<type_of:path>/<filename:path>')
def send_asset(type_of, filename):
    local_path = os.path.join(PROJECT_ROOT,
                              "assets",
                              type_of,
                              filename)
    if os.path.exists(local_path):
        return static_file(filename,
			   root=os.path.join(PROJECT_ROOT,
                                             "assets",
                                             type_of))

@route("/")
def index():
    return template('index.html')




run(host='0.0.0.0',
    port=8142,
    reloader=True)
