#!/usr/bin/env python

# -*- coding: utf-8 -*-

""" Main Spraoi App File"""

import os
import sys
import argparse
import logging
import codecs, json # for reading the mock data

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

__author__ = "Alexander O'Connor <Alexander.OConnor@dcu.ie>"
__credits__ = ["Alexander O'Connor <Alexander.OConnor@dcu.ie>"]
__version__ = "0.1"
__email__ = "Alexander O'Connor <Alex.OConnor@dcu.ie>"
__status__ = "Prototype"

app = Flask(__name__)
api = Api(app)

'''
Argument parser. Used to parse the questions submission (PUT).
'''
parser = reqparse.RequestParser()
parser.add_argument('question_id')
parser.add_argument('answer_choice')

class Questions(Resource):
    '''An API class to handle questions for a specific user.
    GET: retrieves the questions for the provided user.
    PUT: stores the answers for the questions.
    '''
    def get(self, username):
        '''
        Returns the remaining questions for the provided user.
        '''
        if app.config['TESTING'] == True:
            with codecs.open('data.json', 'r', 'utf-8') as f:
                questions = json.loads(f.read())
            return questions

    def put(self, username):
        '''
        TODO: communication with Mongo is probably needed here.
        '''
        args = parser.parse_args()
        print json.dumps(args, indent=4)

api.add_resource(Questions, '/user/quiz/<string:userid>')

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
