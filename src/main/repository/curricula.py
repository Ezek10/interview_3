from collections import defaultdict
from sqlalchemy import delete
from sqlalchemy.sql import select

from src.main.controller.view.curricula import Curricula, Curriculas
from src.main.repository.model.curricula import CurriculaDB
from src.main.repository.config import commit_rollback, db


class CurriculaRepository:
    @staticmethod
    async def create(create_from: Curriculas):
        """create Lead data"""
        for curricula in create_from:
            for subject_id in curricula.subjects_ids:
                db.add(
                    CurriculaDB(carrer_id=curricula.carrer_id, subject_id=subject_id)
                )
        await commit_rollback()

    @staticmethod
    async def delete(carrer_id: int):
        """delete curricula data by carrer id"""

        query = delete(CurriculaDB).where(CurriculaDB.carrer_id == carrer_id)
        await db.execute(query)
        await commit_rollback()

    @staticmethod
    async def get_all() -> Curriculas:
        query = select(CurriculaDB)
        result = (await db.scalars(query)).fetchall()

        curriculas = defaultdict(list)
        for curricula in result:
            curriculas[curricula.carrer_id].append(curricula.subject_id)

        curriculas = Curriculas(
            [Curricula(carrer_id=k, subjects_ids=v) for k, v in curriculas.items()]
        )
        return curriculas
