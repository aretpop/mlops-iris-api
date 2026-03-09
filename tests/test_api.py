from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_prediction():

    data = {
        "features": [5.1, 3.5, 1.4, 0.2]
    }

    response = client.post("/predict", json=data)

    assert response.status_code == 200
    assert "prediction" in response.json()