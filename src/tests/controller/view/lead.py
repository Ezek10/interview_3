import math
from src.main.controller.view.lead import (
    CarrerRegistration,
    CreateLead,
    CreateLeads,
    GetLead,
    GetLeads,
    Person,
    SubjectRegistration,
)
from src.main.schema import PageResponse


class LeadMother:
    @staticmethod
    def create_one(for_response: bool = True) -> CreateLead | GetLead:
        return LeadMother._create_basic_lead(1, for_response)

    @staticmethod
    def create_many(amount: int = 2) -> CreateLeads:
        leads = [
            LeadMother._create_basic_lead(ii, False) for ii in range(1, amount + 1)
        ]
        return CreateLeads(leads)

    @staticmethod
    def create_many_paginated(
        amount: int = 2, page_size: int = 10, page_number: int = 1
    ):
        leads = [LeadMother._create_basic_lead(ii, True) for ii in range(1, amount + 1)]
        response = PageResponse(
            page_number=page_number,
            page_size=page_size,
            total_pages=math.ceil(amount / page_size),
            total_record=amount,
            content=GetLeads(leads),
        )
        return response

    @staticmethod
    def _create_basic_lead(id: int, for_response: bool = False):
        person = LeadMother._create_basic_person(id)
        carrers = [LeadMother._create_basic_carrer(ii) for ii in range(1, 3)]
        subject = [LeadMother._create_basic_subject(ii) for ii in range(1, 6)]
        if for_response:
            return GetLead(person=person, carrers=carrers, subjects=subject, id=id)
        return CreateLead(person=person, carrers=carrers, subjects=subject)

    @staticmethod
    def _create_basic_person(id: int):
        return Person(
            name=f"name_mock_{id}",
            email=f"{id}@mock.com",
            address=f"street {id}",
            phone=f"{id}",
        )

    @staticmethod
    def _create_basic_carrer(id: int):
        return CarrerRegistration(carrer_id=id, registration_year=2000 + id)

    @staticmethod
    def _create_basic_subject(id: int):
        return SubjectRegistration(subject_id=id, attempt=id)
