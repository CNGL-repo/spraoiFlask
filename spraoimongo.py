#!/usr/bin/env python

# -*- coding: utf-8 -*-

""" Spraoi Flask Mongo interface"""

from pymongo import MongoClient
from bson import json_util

import json
import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

def load_configs():
    with open('configs/mongo.json') as f:
        configs = json.load(f)
    return configs

configs = load_configs()

def format_questions(questions):
    '''
    Modifies the structure of the object returned by Mongo to the one expected
    by the UI.
    '''
    res = list()
    for obj in questions:
        question_id = obj['_id']['$oid']
        correct_answer = obj['correctOption']
        answers = [
            obj['option1'],
            obj['option2'],
            obj['option3'],
            obj['option4'],
        ]
        question_str = obj['title']
        
        res.append({
            'question_id': question_id,
            'question_str': question_str,
            'correct_answer': correct_answer,
            'answers': answers
        })
    
    return res

class DB(object):
    
    def __init__(self):
        self.client = None
    
    def connect(self):
        self.client = MongoClient(configs['url'])
        self.db     = self.client[configs['db_name']]
        
        self.questions = self.db['questions']
        self.users     = self.db['users']
        self.answers   = self.db['answers']
    
    def disconnect(self):
        self.client.close()
        self.client = None
    
    def is_connected(self):
        return not self.client is None
    
    def get_questions(self):
        self.connect()
        logging.info("retrieve_questions called")
        res = list(self.questions.find())
        logging.info("retrieve_questions returning %d entries", len(res))
        self.disconnect()
        
        # Make the Object JSON serializable
        json_string = json.dumps(res, sort_keys=True, default=json_util.default)
        questions = json.loads(json_string)
        
        # change the structure a bit as expected by the UI
        return format_questions(questions)

    def store_answers(self, user_id, answers):
        pass