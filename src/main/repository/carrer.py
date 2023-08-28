import math

from sqlalchemy import delete, func
from sqlalchemy.sql import select

from src.main.controller.view.carrer import Carrers
from src.main.repository.config import commit_rollback, db
from src.main.repository.model.carrer import CarrerDB
from src.main.schema import PageResponse


class CarrerRepository:
    @staticmethod
    async def create(create_from: Carrers):
        """create carrer data"""
        for carrer in create_from:
            db.add(CarrerDB(id=carrer.id, name=carrer.name))
        await commit_rollback()

    @staticmethod
    async def delete(carrer_id: int):
        """delete carrer data by id"""

        query = delete(CarrerDB).where(CarrerDB.id == carrer_id)
        await db.execute(query)
        await commit_rollback()

    @staticmethod
    async def get_all(page: int = 1, limit: int = 50) -> PageResponse[Carrers]:
        query = select(CarrerDB)
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
            content=Carrers.model_validate(result),
        )
