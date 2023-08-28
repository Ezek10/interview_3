import math
from src.main.controller.view.carrer import Carrer, Carrers
from src.main.schema import PageResponse


class CarrerMother:
    @staticmethod
    def create_many(amount: int = 5):
        carrers = [CarrerMother._create_basic_carrer(ii) for ii in range(1, amount + 1)]
        return Carrers(carrers)

    @staticmethod
    def create_many_paginated(
        amount: int = 5, page_size: int = 10, page_number: int = 1
    ):
        carrers = Carrers(
            [CarrerMother._create_basic_carrer(ii) for ii in range(1, amount + 1)]
        )
        response = PageResponse(
            page_number=page_number,
            page_size=page_size,
            total_pages=math.ceil(amount / page_size),
            total_record=amount,
            content=carrers,
        )
        return response

    @staticmethod
    def _create_basic_carrer(id):
        return Carrer(id=id, name=f"carrer {id}")
