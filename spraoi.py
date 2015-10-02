#!/usr/bin/env python

# -*- coding: utf-8 -*-

""" Main Spraoi App File"""

import os
import sys
import argparse
import logging
import codecs, json # for reading the mock data

from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_mail import Mail

from spraoimail import send_email_report

__author__ = "Alexander O'Connor <Alexander.OConnor@dcu.ie>"
__credits__ = ["Alexander O'Connor <Alexander.OConnor@dcu.ie>"]
__version__ = "0.1"
__email__ = "Alexander O'Connor <Alex.OConnor@dcu.ie>"
__status__ = "Prototype"

app = Flask(__name__)
app.config.from_object(__name__)
api  = Api(app)
mail = Mail(app)

'''
Mail configurations
'''
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = "spraoiteam@gmail.com"
MAIL_USERNAME = "Spraoi2015"
DEFAULT_MAIL_SENDER = "spraoiteam@gmail.com"

'''
Argument parser. Used to parse the questions submission (PUT).
'''
parser = reqparse.RequestParser()
parser.add_argument('answers', action='append')

class Questions(Resource):
    '''An API class to handle questions for a specific user.
    GET: retrieves the questions for the provided user.
    PUT: stores the answers for the questions.
    '''
    def get(self, userid):
        '''
        Returns the remaining questions for the provided user.
        '''
        if app.config['TESTING'] == True:
            with codecs.open('data.json', 'r', 'utf-8') as f:
                questions = json.loads(f.read())
            return questions

    def put(self, userid):
        '''
        1. Stores the answers
        2. Retrieves the correct answers.
        3. Sends an email report.
        '''
        data = request.get_json()
        chosen_answers = data['answers']
        
        # store in the DB
        for answer in chosen_answers:
            print answer['question'], answer['answer_choice']
        
        # get the correct answers from the DB
        correct_answers = None
        
        send_email_report(mail, "motasim.alsayed@adaptcentre.ie", correct_answers, chosen_answers)
        
        

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
