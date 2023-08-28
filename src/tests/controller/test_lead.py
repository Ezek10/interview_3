from mock import patch, AsyncMock
import pytest
from httpx import AsyncClient
from src.main.app import app
from src.tests.controller.view.lead import LeadMother


@pytest.mark.anyio
@patch("src.main.controller.lead.LeadRepository.create_many")
async def test_create_many(repository: AsyncMock):
    leads = LeadMother.create_many()
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/leads", json=leads.model_dump())
    repository.assert_awaited_once_with(leads)
    assert response.status_code == 200


@pytest.mark.anyio
@patch("src.main.controller.lead.LeadRepository.get_all")
async def test_get_all(repository: AsyncMock):
    leads = LeadMother.create_many_paginated()
    async with AsyncClient(app=app, base_url="http://test") as client:
        repository.return_value = leads
        response = await client.get("/leads")
    repository.assert_awaited_once()
    assert response.status_code == 200
    assert response.json()["result"] == leads.model_dump()


@pytest.mark.anyio
@patch("src.main.controller.lead.LeadRepository.get_by_id")
async def test_get_one(repository: AsyncMock):
    lead = LeadMother.create_one(for_response=True)
    async with AsyncClient(app=app, base_url="http://test") as client:
        repository.return_value = lead
        response = await client.get(f"/leads/lead/{lead.id}")
    repository.assert_awaited_once()
    assert response.status_code == 200
    assert response.json()["result"] == lead.model_dump()


@pytest.mark.anyio
@patch("src.main.controller.lead.LeadRepository.delete")
async def test_delete(repository: AsyncMock):
    id = 1
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.delete(f"/leads/lead/{id}")
    repository.assert_awaited_once_with(id)
    assert response.status_code == 200
