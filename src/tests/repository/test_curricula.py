from mock import AsyncMock, MagicMock, Mock, patch
import pytest
from src.main.repository.curricula import CurriculaRepository
from src.tests.controller.view.curricula import CurriculaMother
from src.tests.repository.model.curricula import CurriculaDBMother


@pytest.mark.asyncio
@patch("src.main.repository.curricula.commit_rollback")
@patch("src.main.repository.curricula.db")
async def test_create_curricula(db: MagicMock, commit: AsyncMock):
    curricula_data = CurriculaMother.create_many(carrer_amount=2, subjects_amount=4)
    db.add = Mock()
    await CurriculaRepository.create(curricula_data)
    assert db.add.call_count == 8
    assert commit.call_count == 1


@pytest.mark.asyncio
@patch("src.main.repository.curricula.commit_rollback")
@patch("src.main.repository.curricula.db")
async def test_delete_curricula(db: AsyncMock, commit: AsyncMock):
    db.execute = AsyncMock()
    await CurriculaRepository.delete(carrer_id=1)
    db.execute.assert_awaited_once()
    assert commit.call_count == 1


@pytest.mark.asyncio
@patch("src.main.repository.curricula.db")
async def test_get_all_curricula(db: AsyncMock):
    carrers_amount = 5
    subjects_amount = 5
    curriculas_db = CurriculaDBMother.create_many(carrers_amount, subjects_amount)

    class ScalarsMock:
        def fetchall(self):
            return curriculas_db

    db.scalars = AsyncMock(return_value=ScalarsMock())
    response = await CurriculaRepository.get_all()
    expected = CurriculaMother.create_many(carrers_amount, subjects_amount)
    db.scalars.assert_awaited_once()
    assert response == expected


def test_repr():
    carrer_id = 1
    curricula_db = CurriculaDBMother._create_one(carrer_id=carrer_id, subject_id=1)
    assert curricula_db.__repr__() == f"CurriculaDB({carrer_id})"
