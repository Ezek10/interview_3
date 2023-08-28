from src.main.controller.view.lead import GetLead, GetLeads
from src.main.repository.model.carrer_register import CarrerRegistrationDB
from src.main.repository.model.person import PersonDB
from src.main.repository.model.subject_register import SubjectRegistrationDB


class LeadDBMother:
    @staticmethod
    def create_many_with_leads(create_from: GetLeads):
        return map(LeadDBMother.create_one_with_lead, create_from)

    @staticmethod
    def create_one_with_lead(create_from: GetLead):
        carrers = LeadDBMother._create_carrer_reg_from_lead(create_from)
        subjects = LeadDBMother._create_subject_reg_from_lead(create_from)
        return PersonDB(
            id=create_from.id,
            name=create_from.person.name,
            email=create_from.person.email,
            address=create_from.person.address,
            phone=create_from.person.phone,
            carrers=carrers,
            subjects=subjects,
        )

    @staticmethod
    def _create_carrer_reg_from_lead(create_from: GetLead):
        return [
            CarrerRegistrationDB(
                person_id=create_from.id,
                carrer_id=carrer.carrer_id,
                registration_year=carrer.registration_year,
            )
            for carrer in create_from.carrers
        ]

    @staticmethod
    def _create_subject_reg_from_lead(create_from: GetLead):
        return [
            SubjectRegistrationDB(
                person_id=create_from.id,
                subject_id=subject.subject_id,
                attempt=subject.attempt,
                course_time=subject.course_time,
            )
            for subject in create_from.subjects
        ]
