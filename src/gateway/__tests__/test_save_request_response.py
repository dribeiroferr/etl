from fastapi.testclient import TestClient

from gateway.application.controllers import app

client = TestClient(app)

def test_save_request():
    request_data = {
        "method": "GET",
        "url": "/test",
        "headers": {"User-Agent": "test"},
        "query_params": {"key": "value"},
        "body": "test body"
    }
    response = client.post("/request/save", json=request_data)
    assert response.status_code == 200
    assert response.json() == {
        "status_code": 200,
        "headers": {},
        "body": {"status": "success"}
    }