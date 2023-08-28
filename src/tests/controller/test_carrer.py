import os
from mock import patch, AsyncMock
import pytest
from httpx import AsyncClient
from src.main.app import app
from src.tests.controller.view.carrer import CarrerMother


@pytest.fixture()
def auth_header():
    os.environ["ADMIN_AUTH"] = "mock_auth"
    return {"admin-auth": "mock_auth"}


@pytest.mark.anyio
@patch("src.main.controller.carrer.CarrerRepository.create")
async def test_create(repository: AsyncMock, auth_header: dict):
    carrers = CarrerMother.create_many()
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/carrers", json=carrers.model_dump(), headers=auth_header
        )
    repository.assert_awaited_once_with(carrers)
    assert response.status_code == 200


@pytest.mark.anyio
@patch("src.main.controller.carrer.CarrerRepository.get_all")
async def test_get(repository: AsyncMock, auth_header: dict):
    carrers = CarrerMother.create_many_paginated()
    async with AsyncClient(app=app, base_url="http://test") as client:
        repository.return_value = carrers
        response = await client.get("/carrers", headers=auth_header)
    repository.assert_awaited_once()
    assert response.status_code == 200
    assert response.json()["result"] == carrers.model_dump()


@pytest.mark.anyio
@patch("src.main.controller.carrer.CarrerRepository.delete")
async def test_delete(repository: AsyncMock, auth_header: dict):
    id = 1
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete(f"/carrers/{id}", headers=auth_header)
    repository.assert_awaited_once_with(id)
    assert response.status_code == 200
