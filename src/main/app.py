from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

from src.main.adapter.controller.whats_app_controller import router
from src.main.domain.exceptions.handler import ProcessException
from src.privacy_policy import MESSAGE

app = FastAPI()
app.include_router(router)


@app.get("/privacy-policy")
async def privacy_policy() -> Response:
    return Response(content=MESSAGE, status_code=200)


@app.get("/status")
async def status() -> Response:
    return Response(content="Status: OK", status_code=200)


@app.get("/")
async def home() -> Response:
    return Response(content="Hola, bienvenido a FinanzasWP", status_code=200)


@app.exception_handler(Exception)
def ExceptionsHandler(request: Request, exception: Exception) -> JSONResponse:
    return ProcessException(request, exception)
