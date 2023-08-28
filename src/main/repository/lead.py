import math

from sqlalchemy import delete, func
from sqlalchemy.sql import select
from sqlalchemy.orm import joinedload

from src.main.controller.view.lead import (
    CarrerRegistration,
    CreateLead,
    CreateLeads,
    GetLead,
    GetLeads,
    Person,
    SubjectRegistration,
)
from src.main.repository.config import commit_rollback, db
from src.main.repository.model.carrer_register import CarrerRegistrationDB
from src.main.repository.model.person import PersonDB
from src.main.repository.model.subject_register import SubjectRegistrationDB
from src.main.schema import PageResponse


class LeadRepository:
    @staticmethod
    async def create_many(create_from: CreateLeads) -> list[int]:
        """create many Lead data"""
        leads_ids = []
        for lead in create_from:
            lead_id = await LeadRepository._add_lead_to_db(lead)
            leads_ids.append(lead_id)
        await commit_rollback()
        return leads_ids

    @staticmethod
    async def _add_lead_to_db(create_from: CreateLead):
        person_db = PersonDB(
            name=create_from.person.name,
            email=create_from.person.email,
            address=create_from.person.address,
            phone=create_from.person.phone,
        )
        db.add(person_db)
        await db.flush()
        for carrer in create_from.carrers:
            db.add(
                CarrerRegistrationDB(
                    person_id=person_db.id,
                    carrer_id=carrer.carrer_id,
                    registration_year=carrer.registration_year,
                )
            )
        for subject in create_from.subjects:
            db.add(
                SubjectRegistrationDB(
                    person_id=person_db.id,
                    subject_id=subject.subject_id,
                    attempt=subject.attempt,
                )
            )
        return person_db.id

    @staticmethod
    async def get_by_id(lead_id: int) -> GetLead:
        """retrieve Lead data by id"""
        query = (
            select(PersonDB)
            .where(PersonDB.id == lead_id)
            .options(joinedload(PersonDB.carrers), joinedload(PersonDB.subjects))
        )
        result = await db.scalar(query)

        if result is None:
            return {}

        return GetLead(
            id=result.id,
            person=Person.model_validate(result),
            carrers=map(CarrerRegistration.model_validate, result.carrers),
            subjects=map(SubjectRegistration.model_validate, result.subjects),
        )

    @staticmethod
    async def delete(lead_id: int):
        """delete Lead data by id"""

        delete_person = delete(PersonDB).where(PersonDB.id == lead_id)
        delete_subjects = delete(CarrerRegistrationDB).where(
            CarrerRegistrationDB.person_id == lead_id
        )
        delete_carrers = delete(SubjectRegistrationDB).where(
            SubjectRegistrationDB.person_id == lead_id
        )
        await db.execute(delete_carrers)
        await db.execute(delete_subjects)
        await db.execute(delete_person)
        await commit_rollback()

    @staticmethod
    async def get_all(page: int = 1, limit: int = 10) -> PageResponse[GetLeads]:
        query = select(PersonDB).options(
            joinedload(PersonDB.carrers), joinedload(PersonDB.subjects)
        )
        count_query = select(func.count(1)).select_from(query)

        offset_page = page - 1
        query = query.offset(offset_page * limit).limit(limit)
        total_record = await db.scalar(count_query)
        total_page = math.ceil(total_record / limit)
        result = (await db.scalars(query)).unique()

        leads = (
            []
            if result is None
            else (
                GetLeads(
                    [
                        GetLead(
                            id=lead.id,
                            person=Person.model_validate(lead),
                            carrers=map(
                                CarrerRegistration.model_validate, lead.carrers
                            ),
                            subjects=map(
                                SubjectRegistration.model_validate, lead.subjects
                            ),
                        )
                        for lead in result
                    ]
                )
            )
        )

        return PageResponse(
            page_number=page,
            page_size=limit,
            total_pages=total_page,
            total_record=total_record,
            content=leads,
        )
