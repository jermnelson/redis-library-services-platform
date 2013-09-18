__author__ = "Jeremy Nelson"

from distutils.core import setup
import os
import py2exe

setup(name='rlsp',
      version='0.5.0',
      description="""The Redis Library Services Platform is made up of two
projects; the Aristotle Library Apps and the BIBFRAME Datastore for managing a semantic server with a web portal""",
      author="Jeremy Nelson",
      author_email="jermnelson@gmail.com",
      url="https://github.com/jermnelson/redis-library-services-platform",
      console=['rlsp.py'],
      packages=['aristotle-library-apps'])
