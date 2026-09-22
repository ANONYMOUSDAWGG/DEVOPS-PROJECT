import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "UP"


def test_get_products(client):
    resp = client.get("/products")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 3


def test_get_product_found(client):
    resp = client.get("/products/101")
    assert resp.status_code == 200
    assert resp.get_json()["name"] == "Wireless Mouse"


def test_get_product_not_found(client):
    resp = client.get("/products/999")
    assert resp.status_code == 404
