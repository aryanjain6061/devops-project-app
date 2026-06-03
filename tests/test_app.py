import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json['status'] == 'ok'

def test_hello(client):
    res = client.get('/api/v1/hello')
    assert res.status_code == 200
    assert 'message' in res.json

def test_version(client):
    res = client.get('/api/v1/version')
    assert res.status_code == 200
    assert res.json['version'] == '1.0.0'
