import spraoi
import json

import pytest

@pytest.fixture
def client(request):
    spraoi.app.config['TESTING'] = True;
    client = spraoi.app.test_client()
    return client

def hello_world_client(client):
    return client.get('/hello', follow_redirects = True)

def hello_user_client(client, username):
    return client.get('/hello', data=dict(username = username))

def test_hello(client):
    """ Test hello world"""
    result = hello_world_client(client)
    resultJSON = json.loads(result.data)
    assert resultJSON['hello'] == 'hello'

def test_hello_user(client):
    """ Test hello world"""
    result = hello_user_(client, 'user')
    resultJSON = json.loads(result.data)
    assert resultJSON['name'] == 'user'

def user_completed(client, email):
    return client.get('/user', data=dict(email=email))

def test_user_completed(client):

