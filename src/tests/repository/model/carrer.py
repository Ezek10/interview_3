from src.main.controller.view.carrer import Carrer, Carrers
from src.main.repository.model.carrer import CarrerDB


class CarrerDBMother:
    @staticmethod
    def create_many_with_carrers(create_from: Carrers):
        return map(CarrerDBMother._create_one_with_carrer, create_from)

    @staticmethod
    def _create_one_with_carrer(create_from: Carrer):
        return CarrerDB(id=create_from.id, name=create_from.name)
