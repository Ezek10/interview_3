from mock import AsyncMock, MagicMock, Mock, patch
import pytest
from src.main.repository.lead import LeadRepository
from src.main.schema import PageResponse
from src.tests.controller.view.lead import LeadMother
from src.tests.repository.model.lead import LeadDBMother


@pytest.mark.asyncio
@patch("src.main.repository.lead.commit_rollback")
@patch("src.main.repository.lead.db")
async def test_create_lead(db: MagicMock, commit: AsyncMock):
    amount = 4
    lead_data = LeadMother.create_many(amount)
    db.add = Mock()
    db.flush = AsyncMock()
    response = await LeadRepository.create_many(lead_data)
    assert response == [None for _ in range(amount)]
    assert db.add.call_count == amount * (
        1 + len(lead_data[0].carrers) + len(lead_data[0].subjects)
    )
    assert db.flush.call_count == amount
    assert commit.call_count == 1


@pytest.mark.asyncio
@patch("src.main.repository.lead.commit_rollback")
@patch("src.main.repository.lead.db")
async def test_delete_lead(db: AsyncMock, commit: AsyncMock):
    db.execute = AsyncMock()
    await LeadRepository.delete(1)
    assert db.execute.call_count == 3
    assert commit.call_count == 1


@pytest.mark.asyncio
@patch("src.main.repository.lead.db")
async def test_get_one_lead(db: AsyncMock):
    lead = LeadMother.create_one(for_response=True)
    lead_db = LeadDBMother().create_one_with_lead(lead)
    db.scalar = AsyncMock(return_value=lead_db)
    response = await LeadRepository.get_by_id(lead.id)
    db.scalar.assert_awaited_once()
    assert response == lead


@pytest.mark.asyncio
@patch("src.main.repository.lead.db")
async def test_get_one_lead_not_exist(db: AsyncMock):
    db.scalar = AsyncMock(return_value=None)
    response = await LeadRepository.get_by_id(1)
    db.scalar.assert_awaited_once()
    assert response == {}


@pytest.mark.asyncio
@patch("src.main.repository.lead.db")
async def test_get_all_lead(db: AsyncMock):
    amount = 5
    leads = LeadMother.create_many_paginated(amount)
    leads_db = LeadDBMother().create_many_with_leads(leads.content)

    class ScalarsMock:
        def unique(self):
            return leads_db

    db.scalar = AsyncMock(return_value=amount)
    db.scalars = AsyncMock(return_value=ScalarsMock())
    response = await LeadRepository.get_all(page=1, limit=10)
    db.scalar.assert_awaited_once()
    db.scalars.assert_awaited_once()
    assert response == leads


@pytest.mark.asyncio
@patch("src.main.repository.lead.db")
async def test_get_all_lead_not_exist(db: AsyncMock):
    class ScalarsMock:
        def unique(self):
            return None

    db.scalar = AsyncMock(return_value=0)
    db.scalars = AsyncMock(return_value=ScalarsMock())
    response = await LeadRepository.get_all(page=1, limit=10)
    expected = PageResponse(
        page_number=1, page_size=10, total_pages=0, total_record=0, content=[]
    )
    db.scalar.assert_awaited_once()
    db.scalars.assert_awaited_once()
    assert response == expected


def test_lead_repr():
    lead = LeadMother.create_one()
    lead_db = LeadDBMother.create_one_with_lead(lead)
    assert lead_db.__repr__() == f"PersonDB({lead_db.id})"
    assert (
        lead_db.carrers[0].__repr__()
        == f"CarrerRegistrationDB({lead_db.carrers[0].id})"
    )
    assert (
        lead_db.subjects[0].__repr__()
        == f"SubjectRegistrationDB({lead_db.subjects[0].id})"
    )
