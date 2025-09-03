import pytest
from fastapi.testclient import TestClient
from app.main import app  # your product service main.py

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Product Service running 🚀"}

def test_create_product(client):
    response = client.post(
        "/products/",
        json={"name": "Laptop", "price": 999.99, "stock": 10}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 999.99
    assert "id" in data
