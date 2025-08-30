from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_register_and_login():
    r = client.post('/auth/register', json={'email': 'a@example.com', 'password': 'secret'})
    assert r.status_code == 200
    r = client.post('/auth/login', json={'email': 'a@example.com', 'password': 'secret'})
    assert r.status_code == 200
    token = r.json()['access_token']
    assert token
