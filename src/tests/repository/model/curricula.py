from src.main.repository.model.curricula import CurriculaDB


class CurriculaDBMother:
    @staticmethod
    def create_many(carrers_amount: int = 2, subjects_amount: int = 4):
        curriculas = [
            CurriculaDBMother._create_one(carrer_id=cc, subject_id=ss)
            for cc in range(1, carrers_amount + 1)
            for ss in range(1, subjects_amount + 1)
        ]
        return curriculas

    @staticmethod
    def _create_one(carrer_id: int, subject_id: int):
        return CurriculaDB(carrer_id=carrer_id, subject_id=subject_id)
