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

import spraoimongo

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
        else:
            if mongoGetUser(email):
                response = {'completed':'True'}
            else:
                response = {'completed':'False'}
        return response

api.add_resource(User, '/user/<string:email>')

class Quiz(Resource):
    def get(self):
        if app.config['TESTING'] == True:
            #Sorry for the broken formatting
                questions = [{
                    "answers": [
                        {"0":"Not much, really."},
                        {"1":"Oh, nothing interesting"},
                        {"2":"Just wanted to say hi."},
                        {"3":"There's no 4th answer."}
                    ],
                    "question_id": 1,
                    "question_str": "What's up?",
                    "correct_answer":"0"
                    },
                    {
                    "answers": [
                        {"0":"Man U."},
                        {"1":"Barcelona."},
                        {"2":"Bayern Munich."},
                        {"3":"Liverpool."}
                    ],
                    "question_id": 2,
                    "question_str": "What's your favorite team?",
                    "correct_answer":"1"
                    },
                {
                    "answers": [
                        {"0","Dublin."},
                        {"1","Galway."},
                        {"2","Donegal."},
                        {"3","Belfast."}
                    ],
                    "question_id": 2,
                    "question_str": "What's your favorite city?",
                    "correct_answer":"1"
                    }
                ]
                response = questions
        else:
            response = spraoimongo.mongoGetQuestions()
        return response

api.add_resource(Quiz, '/questions')

if __name__ == "__main__":
    app.run(debug=True)
