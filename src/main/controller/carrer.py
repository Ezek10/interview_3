from fastapi import Depends
from fastapi.routing import APIRouter
from src.main.authorization.admin import verify_key

from src.main.controller.view.carrer import Carrers
from src.main.repository.carrer import CarrerRepository
from src.main.schema import PageResponse, ResponseSchema

router = APIRouter(prefix="/carrers", tags=["carrer"])


@router.post("", response_model=ResponseSchema, dependencies=[Depends(verify_key)])
async def create_carrers(create_from: Carrers):
    result = await CarrerRepository.create(create_from)
    return ResponseSchema(detail="Successfully created data !", result=result)


@router.delete(
    "/{carrer_id}", response_model=ResponseSchema, dependencies=[Depends(verify_key)]
)
async def delete_carrer(carrer_id: int):
    await CarrerRepository.delete(carrer_id)
    return ResponseSchema(detail="Successfully deleted data !")


@router.get(
    "",
    response_model=ResponseSchema[PageResponse[Carrers]],
    dependencies=[Depends(verify_key)],
)
async def get_all_carrers():
    result = await CarrerRepository.get_all()
    return ResponseSchema(
        detail="Successfully fetch Carrer data by id !", result=result
    )
