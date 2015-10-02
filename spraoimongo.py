#!/usr/bin/env python

# -*- coding: utf-8 -*-

""" Spraoi Flask Mongo interface"""

from pymongo import MongoClient

def connect_db(uri, db_name):
    return MongoClient(uri)[db_name]

def mongoGetUser(username):
    pass

def mongoPutQuiz(username, answers):
    pass


