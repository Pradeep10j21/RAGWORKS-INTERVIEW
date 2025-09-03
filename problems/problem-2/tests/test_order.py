import pytest
from fastapi.testclient import TestClient
from app.main import app  # your order service main.py

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Order Service running 🚀"}

def test_create_order(client):
    response = client.post(
        "/orders/",
        json={"user_id": 1, "product_id": 1, "quantity": 2}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 1
    assert data["product_id"] == 1
    assert data["quantity"] == 2
    assert "id" in data
