import math
from src.main.controller.view.subject import Subject, Subjects
from src.main.schema import PageResponse


class SubjectMother:
    @staticmethod
    def create_many(amount: int = 5):
        subjects = [
            SubjectMother._create_basic_subject(ii) for ii in range(1, amount + 1)
        ]
        return Subjects(subjects)

    @staticmethod
    def create_many_paginated(
        amount: int = 5, page_size: int = 10, page_number: int = 1
    ):
        subjects = Subjects(
            [SubjectMother._create_basic_subject(ii) for ii in range(1, amount + 1)]
        )
        response = PageResponse(
            page_number=page_number,
            page_size=page_size,
            total_pages=math.ceil(amount / page_size),
            total_record=amount,
            content=subjects,
        )
        return response

    @staticmethod
    def _create_basic_subject(id):
        return Subject(id=id, name=f"subject {id}")
