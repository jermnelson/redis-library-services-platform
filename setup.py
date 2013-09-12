__author__ = "Jeremy Nelson"

from distutils.core import setup
import os
import py2exe

setup(console=[os.path.join('aristotle-library-apps',
                            'manage.py')])
