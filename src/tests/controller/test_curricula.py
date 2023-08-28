import os
from mock import patch, AsyncMock
import pytest
from httpx import AsyncClient
from src.main.app import app
from src.tests.controller.view.curricula import CurriculaMother


@pytest.fixture()
def auth_header():
    os.environ["ADMIN_AUTH"] = "mock_auth"
    return {"admin-auth": "mock_auth"}


@pytest.mark.anyio
@patch("src.main.controller.curricula.CurriculaRepository.create")
async def test_create(repository: AsyncMock, auth_header: dict):
    curriculas = CurriculaMother.create_many()
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/curriculas", json=curriculas.model_dump(), headers=auth_header
        )
    repository.assert_awaited_once_with(curriculas)
    assert response.status_code == 200


@pytest.mark.anyio
@patch("src.main.controller.curricula.CurriculaRepository.get_all")
async def test_get(repository: AsyncMock, auth_header: dict):
    curriculas = CurriculaMother.create_many()
    async with AsyncClient(app=app, base_url="http://test") as client:
        repository.return_value = curriculas
        response = await client.get("/curriculas", headers=auth_header)
    repository.assert_awaited_once()
    assert response.status_code == 200
    assert response.json()["result"] == curriculas.model_dump()


@pytest.mark.anyio
@patch("src.main.controller.curricula.CurriculaRepository.delete")
async def test_delete(repository: AsyncMock, auth_header: dict):
    carrer_id = 1
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete(f"/curriculas/{carrer_id}", headers=auth_header)
    repository.assert_awaited_once_with(carrer_id)
    assert response.status_code == 200
