import os
from mock import patch, AsyncMock
import pytest
from httpx import AsyncClient
from src.main.app import app
from src.tests.controller.view.subject import SubjectMother


@pytest.fixture()
def auth_header():
    os.environ["ADMIN_AUTH"] = "mock_auth"
    return {"admin-auth": "mock_auth"}


@pytest.mark.anyio
@patch("src.main.controller.subject.SubjectRepository.create")
async def test_create(repository: AsyncMock, auth_header: dict):
    subjects = SubjectMother.create_many()
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/subjects", json=subjects.model_dump(), headers=auth_header
        )
    repository.assert_awaited_once_with(subjects)
    assert response.status_code == 200


@pytest.mark.anyio
@patch("src.main.controller.subject.SubjectRepository.get_all")
async def test_get(repository: AsyncMock, auth_header: dict):
    subjects = SubjectMother.create_many_paginated()
    async with AsyncClient(app=app, base_url="http://test") as client:
        repository.return_value = subjects
        response = await client.get("/subjects", headers=auth_header)
    repository.assert_awaited_once()
    assert response.status_code == 200
    assert response.json()["result"] == subjects.model_dump()


@pytest.mark.anyio
@patch("src.main.controller.subject.SubjectRepository.delete")
async def test_delete(repository: AsyncMock, auth_header: dict):
    id = 1
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete(f"/subjects/{id}", headers=auth_header)
    repository.assert_awaited_once_with(id)
    assert response.status_code == 200
