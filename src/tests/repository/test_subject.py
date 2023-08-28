from mock import AsyncMock, MagicMock, Mock, patch
import pytest
from src.main.repository.subject import SubjectRepository
from src.tests.controller.view.subject import SubjectMother
from src.tests.repository.model.subject import SubjectDBMother


@pytest.mark.asyncio
@patch("src.main.repository.subject.commit_rollback")
@patch("src.main.repository.subject.db")
async def test_create_subject(db: MagicMock, commit: AsyncMock):
    amount = 4
    subject_data = SubjectMother.create_many(amount)
    db.add = Mock()
    await SubjectRepository.create(subject_data)
    assert db.add.call_count == amount
    assert commit.call_count == 1


@pytest.mark.asyncio
@patch("src.main.repository.subject.commit_rollback")
@patch("src.main.repository.subject.db")
async def test_delete_subject(db: AsyncMock, commit: AsyncMock):
    db.execute = AsyncMock()
    await SubjectRepository.delete(1)
    db.execute.assert_awaited_once()
    assert commit.call_count == 1


@pytest.mark.asyncio
@patch("src.main.repository.subject.db")
async def test_get_all_subject(db: AsyncMock):
    amount = 5
    subjects = SubjectMother.create_many_paginated(amount)
    subjects_db = SubjectDBMother.create_many_with_subjects(subjects.content)

    class ScalarsMock:
        def fetchall(self):
            return subjects_db

    db.scalar = AsyncMock(return_value=amount)
    db.scalars = AsyncMock(return_value=ScalarsMock())
    response = await SubjectRepository.get_all(page=1, limit=10)
    db.scalar.assert_awaited_once()
    db.scalars.assert_awaited_once()
    assert response == subjects


def test_subjectdb_repr():
    subject = SubjectMother._create_basic_subject(1)
    subject_db = SubjectDBMother._create_one_with_subject(subject)
    assert subject_db.__repr__() == f"SubjectDB({subject_db.id})"
