from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Bienvenido" in response.json()["message"]


def test_time():
    response = client.get("/time")
    assert response.status_code == 200
    assert "time" in response.json()
    assert "source" in response.json()
