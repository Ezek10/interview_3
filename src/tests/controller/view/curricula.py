from src.main.controller.view.curricula import Curricula, Curriculas


class CurriculaMother:
    @staticmethod
    def create_many(carrer_amount: int = 2, subjects_amount: int = 4):
        curriculas = [
            CurriculaMother._create_basic_curricula(
                carrer_id=ii, subjects_amount=subjects_amount
            )
            for ii in range(1, carrer_amount + 1)
        ]
        return Curriculas(curriculas)

    @staticmethod
    def _create_basic_curricula(carrer_id: int, subjects_amount: int):
        return Curricula(
            carrer_id=carrer_id,
            subjects_ids=[ii for ii in range(1, subjects_amount + 1)],
        )
