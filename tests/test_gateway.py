from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chat_endpoint_returns_gateway_response():
    response = client.post(
        "/v1/chat",
        json={"messages": [{"role": "user", "content": "hello"}]},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["content"] == "Gateway response: hello"
    assert body["input_tokens"] > 0
    assert body["output_tokens"] > 0
    assert body["cost_cny"] >= 0


def test_structured_endpoint_validates_schema():
    response = client.post(
        "/v1/structured",
        json={
            "messages": [{"role": "user", "content": "extract_profile"}],
            "schema": {
                "type": "object",
                "required": ["name", "role", "goal"],
                "properties": {
                    "name": {"type": "string"},
                    "role": {"type": "string"},
                    "goal": {"type": "string"},
                },
            },
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["data"]["name"] == "Alex"
    assert body["retries"] == 0


def test_structured_endpoint_rejects_invalid_json_after_retries():
    response = client.post(
        "/v1/structured",
        json={
            "messages": [{"role": "user", "content": "return_invalid_json"}],
            "schema": {"type": "object"},
            "max_retries": 1,
        },
    )

    assert response.status_code == 422


def test_usage_endpoint_tracks_requests():
    before = client.get("/v1/usage").json()["request_count"]
    client.post("/v1/chat", json={"messages": [{"role": "user", "content": "usage check"}]})
    after = client.get("/v1/usage").json()["request_count"]

    assert after == before + 1
