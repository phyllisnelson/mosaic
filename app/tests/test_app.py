from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_app_missing_model_year():
    uri = "/electric-ranges"
    response = client.get(uri)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["query", "model_year"],
                "msg": "Field required",
                "input": None,
            }
        ]
    }


def test_app_wrong_type_model_year():
    model_year = "aaaa"
    uri = f"/electric-ranges?model_year={model_year}"
    response = client.get(uri)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": model_year,
                "loc": ["query", "model_year"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "type": "int_parsing",
            }
        ]
    }


# TODO: parametrize with multiple years and results
def test_app():
    model_year = "2025"
    uri = f"/electric-ranges?model_year={model_year}"
    response = client.get(uri)

    assert response.status_code == 200
    assert {
        "electric_range": {"count": 156, "mean": 29.743589743589745},
        "make": "BMW",
    } in response.json()["results"]


# TODO: Add test for unresponsive WA GOV endpoint
# TODO: Add test for bad response from WA GOV endpoint
# TODO: Add test for non-existent model year
