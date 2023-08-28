from fastapi.routing import APIRouter

from src.main.controller.view.lead import CreateLeads, GetLead, GetLeads
from src.main.repository.lead import LeadRepository
from src.main.schema import PageResponse, ResponseSchema

router = APIRouter(prefix="/leads", tags=["lead"])


@router.post("", response_model=ResponseSchema)
async def create_leads(create_from: CreateLeads):
    result = await LeadRepository.create_many(create_from)
    return ResponseSchema(detail="Successfully created data !", result=result)


@router.delete("/lead/{lead_id}", response_model=ResponseSchema)
async def delete_lead(lead_id: int):
    await LeadRepository.delete(lead_id)
    return ResponseSchema(detail="Successfully deleted data !")


@router.get("/lead/{lead_id}", response_model=ResponseSchema[GetLead])
async def get_lead_by_id(lead_id: int):
    result = await LeadRepository.get_by_id(lead_id)
    return ResponseSchema(detail="Successfully fetch lead data by id !", result=result)


@router.get("", response_model=ResponseSchema[PageResponse[GetLeads]])
async def get_all_lead(
    page: int = 1,
    limit: int = 10,
):
    result = await LeadRepository.get_all(page, limit)
    return ResponseSchema(detail="Successfully fetch lead data by id !", result=result)
