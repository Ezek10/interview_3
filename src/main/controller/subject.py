from fastapi import Depends
from fastapi.routing import APIRouter
from src.main.authorization.admin import verify_key
from src.main.controller.view.subject import Subjects
from src.main.repository.subject import SubjectRepository
from src.main.schema import PageResponse, ResponseSchema

router = APIRouter(prefix="/subjects", tags=["subject"])


@router.post("", response_model=ResponseSchema, dependencies=[Depends(verify_key)])
async def create_subjects(create_from: Subjects):
    result = await SubjectRepository.create(create_from)
    return ResponseSchema(detail="Successfully created data !", result=result)


@router.delete(
    "/{subject_id}", response_model=ResponseSchema, dependencies=[Depends(verify_key)]
)
async def delete_subject(subject_id: int):
    await SubjectRepository.delete(subject_id)
    return ResponseSchema(detail="Successfully deleted data !")


@router.get(
    "",
    response_model=ResponseSchema[PageResponse[Subjects]],
    dependencies=[Depends(verify_key)],
)
async def get_all_subjects():
    result = await SubjectRepository.get_all()
    return ResponseSchema(
        detail="Successfully fetch Subject data by id !", result=result
    )
