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


def test_get_users(client):
    resp = client.get("/users")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 3


def test_get_user_found(client):
    resp = client.get("/users/1")
    assert resp.status_code == 200
    assert resp.get_json()["name"] == "Aarav Shah"


def test_get_user_not_found(client):
    resp = client.get("/users/999")
    assert resp.status_code == 404
