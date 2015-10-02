#!/usr/bin/env python

# -*- coding: utf-8 -*-

""" Spraoi Flask Mongo interface"""

from pymongo import MongoClient

def connect_db(uri, db_name):
    return MongoClient(uri)[db_name]

def mongoGetUser(email):
    user_collection = connect_db['users']
    return user.collection.find_one({'email':email})

def mongoGetQuestions():
    pass

def mongoPutQuiz(username, answers):
    pass
