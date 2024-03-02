from fastapi.testclient import TestClient
from .main import app
import json
client = TestClient(app)

def test_read():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello" : "World"}

def test_items_read_item_success():
    response = client.get("/items/1234")
    assert response.status_code == 200

def test_items_raise_validation_error():
    response = client.get("/items/abrar")
    response.status_code == 422
    data = json.loads(response.text)
    error = data.get("detail")[0]
    assert error.get("msg") == "value is not a valid integer"