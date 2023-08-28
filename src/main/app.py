from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

from src.main.controller.lead import router as lead_router
from src.main.controller.carrer import router as carrer_router
from src.main.controller.subject import router as subject_router
from src.main.controller.curricula import router as curricula_router
from src.main.exceptions.handler import ProcessException
from src.main.repository.config import db


app = FastAPI()

app.include_router(lead_router)
app.include_router(carrer_router)
app.include_router(subject_router)
app.include_router(curricula_router)


@app.on_event("startup")
async def startup():
    db.init()
    await db.create_all()


@app.on_event("shutdown")
async def shutdown():
    await db.close()


@app.get("/status")
async def status() -> Response:
    return Response(content="Status: OK", status_code=200)


@app.get("/")
async def home() -> Response:
    return Response(content="Welcome Home", status_code=200)


@app.exception_handler(Exception)
def ExceptionsHandler(request: Request, exception: Exception) -> JSONResponse:
    """Exception Handler for all the app"""
    return ProcessException(request, exception)
