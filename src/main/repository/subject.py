import math

from sqlalchemy import delete, func
from sqlalchemy.sql import select
from src.main.controller.view.subject import Subjects
from src.main.repository.config import commit_rollback, db
from src.main.repository.model.subject import SubjectDB
from src.main.schema import PageResponse


class SubjectRepository:
    @staticmethod
    async def create(create_from: Subjects):
        """create Lead data"""
        for subject in create_from:
            db.add(SubjectDB(id=subject.id, name=subject.name))

        await commit_rollback()

    @staticmethod
    async def delete(subject_id: int):
        """delete subject data by id"""

        query = delete(SubjectDB).where(SubjectDB.id == subject_id)
        await db.execute(query)
        await commit_rollback()

    @staticmethod
    async def get_all(page: int = 1, limit: int = 50) -> PageResponse[Subjects]:
        query = select(SubjectDB)
        count_query = select(func.count(1)).select_from(query)
        offset_page = page - 1
        query = query.offset(offset_page * limit).limit(limit)
        total_record = await db.scalar(count_query)
        total_page = math.ceil(total_record / limit)
        result = (await db.scalars(query)).fetchall()

        return PageResponse(
            page_number=page,
            page_size=limit,
            total_pages=total_page,
            total_record=total_record,
            content=Subjects.model_validate(result),
        )
