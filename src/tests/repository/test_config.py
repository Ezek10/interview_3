import os
from mock import AsyncMock, patch, Mock
import pytest
from sqlalchemy.exc import IntegrityError
from src.main.exceptions.already_exist_exception import AlreadyExistException
from src.main.repository.config import db, commit_rollback


@pytest.mark.asyncio
@patch("src.main.repository.config.create_async_engine")
async def test_config_db_init(create_engine: Mock):
    os.environ["DB_ENGINE"] = ""
    os.environ["DB_USERNAME"] = ""
    os.environ["DB_PASSWORD"] = ""
    os.environ["DB_HOST"] = ""
    os.environ["DB_PORT"] = ""
    os.environ["DB_NAME"] = ""
    db.init()
    create_engine.assert_called_once()


@pytest.mark.asyncio
@patch("src.main.repository.config.db")
async def test_config_commit_ok(db: AsyncMock):
    db.commit = AsyncMock()
    await commit_rollback()
    db.commit.assert_awaited_once()


@pytest.mark.asyncio
@patch("src.main.repository.config.db")
async def test_config_commit_integrity_error(db: AsyncMock):
    db.commit = AsyncMock()

    def raise_exception():
        raise IntegrityError(statement="", params="", orig="")

    db.commit.side_effect = raise_exception
    db.rollback = AsyncMock()
    with pytest.raises(AlreadyExistException):
        await commit_rollback()
    db.commit.assert_awaited_once()
    db.rollback.assert_awaited_once()


@pytest.mark.asyncio
@patch("src.main.repository.config.db")
async def test_config_commit_error(db: AsyncMock):
    db.commit = AsyncMock()

    def raise_exception():
        raise Exception()

    db.commit.side_effect = raise_exception
    db.rollback = AsyncMock()
    with pytest.raises(Exception):
        await commit_rollback()
    db.commit.assert_awaited_once()
    db.rollback.assert_awaited_once()
