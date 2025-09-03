import pytest
from fastapi.testclient import TestClient
from app.main import app  # your user service main.py

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "User Service running 🚀"}

def test_create_user(client):
    response = client.post(
        "/users/",
        json={"username": "alice", "email": "alice@example.com", "password": "pass123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    assert "id" in data
