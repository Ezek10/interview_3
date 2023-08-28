from fastapi.testclient import TestClient
from mock import Mock, patch
import pytest

from src.main.app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_status():
    response = client.get("/status")
    assert response.status_code == 200


@patch("src.main.app.ProcessException")
@patch("src.main.app.Response")
def test_exc(response: Mock, process_exc: Mock):
    def raise_exception(**kwargs):
        raise Exception()

    response.side_effect = raise_exception
    with pytest.raises(Exception):
        client.get("/status")
    process_exc.assert_called_once()
