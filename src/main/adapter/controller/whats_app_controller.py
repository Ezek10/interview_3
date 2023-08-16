from datetime import datetime

from fastapi import Request, Response
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.main.adapter.controller.request.whats_app_request import WPRequest
from src.main.usecases.process_message_use_case import ProcessMessageUseCase

router = APIRouter(prefix="/whats_app")


@router.get("")
async def verification(request: Request):
    print(request.query_params)
    response = request.query_params["hub.challenge"]
    return Response(status_code=200, content=response)


@router.post("")
async def read_message(request: WPRequest):
    print("-------------REQUEST-----------")
    print(request)
    message = request.entry[0].changes[0].value.messages[0]
    phone = message.from_
    timestamp = int(message.timestamp)
    body = message.text.body
    date = datetime.fromtimestamp(timestamp)
    ProcessMessageUseCase().execute(phone=phone, message=body, date=date)
    return JSONResponse(status_code=200, content="")
