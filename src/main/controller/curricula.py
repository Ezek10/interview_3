from fastapi import Depends
from fastapi.routing import APIRouter
from src.main.authorization.admin import verify_key

from src.main.controller.view.curricula import Curriculas
from src.main.repository.curricula import CurriculaRepository
from src.main.schema import ResponseSchema

router = APIRouter(prefix="/curriculas", tags=["curricula"])


@router.post("", response_model=ResponseSchema, dependencies=[Depends(verify_key)])
async def create_curriculas(create_from: Curriculas):
    result = await CurriculaRepository.create(create_from)
    return ResponseSchema(detail="Successfully created data !", result=result)


@router.delete(
    "/{carrer_id}", response_model=ResponseSchema, dependencies=[Depends(verify_key)]
)
async def delete_curricula(carrer_id: int):
    await CurriculaRepository.delete(carrer_id)
    return ResponseSchema(detail="Successfully deleted data !")


@router.get(
    "", response_model=ResponseSchema[Curriculas], dependencies=[Depends(verify_key)]
)
async def get_all_curriculas():
    result = await CurriculaRepository.get_all()
    return ResponseSchema(
        detail="Successfully fetch Curricula data by id !", result=result
    )
