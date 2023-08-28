from mock import AsyncMock, MagicMock, Mock, patch
import pytest
from src.main.repository.carrer import CarrerRepository
from src.tests.controller.view.carrer import CarrerMother
from src.tests.repository.model.carrer import CarrerDBMother


@pytest.mark.asyncio
@patch("src.main.repository.carrer.commit_rollback")
@patch("src.main.repository.carrer.db")
async def test_create_carrer(db: MagicMock, commit: AsyncMock):
    amount = 4
    carrer_data = CarrerMother.create_many(amount)
    db.add = Mock()
    await CarrerRepository.create(carrer_data)
    assert db.add.call_count == amount
    assert commit.call_count == 1


@pytest.mark.asyncio
@patch("src.main.repository.carrer.commit_rollback")
@patch("src.main.repository.carrer.db")
async def test_delete_carrer(db: AsyncMock, commit: AsyncMock):
    db.execute = AsyncMock()
    await CarrerRepository.delete(1)
    db.execute.assert_awaited_once()
    assert commit.call_count == 1


@pytest.mark.asyncio
@patch("src.main.repository.carrer.db")
async def test_get_all_carrer(db: AsyncMock):
    amount = 5
    carrers = CarrerMother.create_many_paginated(amount)
    carrers_db = CarrerDBMother.create_many_with_carrers(carrers.content)

    class ScalarsMock:
        def fetchall(self):
            return carrers_db

    db.scalar = AsyncMock(return_value=amount)
    db.scalars = AsyncMock(return_value=ScalarsMock())
    response = await CarrerRepository.get_all(page=1, limit=10)
    db.scalar.assert_awaited_once()
    db.scalars.assert_awaited_once()
    assert response == carrers


def test_carrerdb_repr():
    carrer = CarrerMother._create_basic_carrer(1)
    carrer_db = CarrerDBMother._create_one_with_carrer(carrer)
    assert carrer_db.__repr__() == f"CarrerDB({carrer_db.id})"
