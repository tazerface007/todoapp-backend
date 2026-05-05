from app import create_app
from fastapi.testclient import TestClient


app = create_app()

client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200


def test_read_home():
    response = client.get('/')
    assert response.status_code == 200
    print(f'Response: {response.json()}')
    assert response.json() == {'message': 'Welcome to home'}

