import spraoi
import json

import pytest

@pytest.fixture
def client(request):
    spraoi.app.config['TESTING'] = True;
    client = spraoi.app.test_client()
    return client

def user_completed(client, email):
    return client.get('/user/quiz', data=dict(email=email))

def test_user_completed(client):
    print user_completed(client, 'completeduser@example.com').data['completed']
    assert False
