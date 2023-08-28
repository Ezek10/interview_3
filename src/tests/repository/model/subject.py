from src.main.controller.view.subject import Subject, Subjects
from src.main.repository.model.subject import SubjectDB


class SubjectDBMother:
    @staticmethod
    def create_many_with_subjects(create_from: Subjects):
        return map(SubjectDBMother._create_one_with_subject, create_from)

    @staticmethod
    def _create_one_with_subject(create_from: Subject):
        return SubjectDB(id=create_from.id, name=create_from.name)
