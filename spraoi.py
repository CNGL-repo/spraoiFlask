
#!/usr/bin/env python

# -*- coding: utf-8 -*-

""" Main Spraoi App File"""

import os
import sys
import argparse
import logging

from flask import Flask, jsonify
from flask_restful import Resource, Api

__author__ = "Alexander O'Connor <Alexander.OConnor@dcu.ie>"
__credits__ = ["Alexander O'Connor <Alexander.OConnor@dcu.ie>"]
__version__ = "0.1"
__email__ = "Alexander O'Connor <Alex.OConnor@dcu.ie>"
__status__ = "Prototype"

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello':'hello','name':'world'}

class HelloName(Resource):
    def get(self, username):
        return {'hello':'hello', 'name': username}

api.add_resource(HelloName, '/hello/<string:username>')
api.add_resource(HelloWorld, '/hello')

class User(Resource):
    def get(self, email):
        if app.config['TESTING'] == True:
            print "testing"
            if email == "completeduser@exmaple.com":
                response = {'completed':'True'}
            else:
                response = {'completed' : 'False'}
            return response
        else:
            return {'error':'not implemented'}
        return jsonify(hello='hello', name='world')

api.add_resource(User, '/user/<string:email>')

if __name__ == "__main__":
    app.run(debug=True)
