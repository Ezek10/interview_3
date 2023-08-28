from fastapi import Request
from fastapi.responses import JSONResponse

from src.main.exceptions.already_exist_exception import AlreadyExistException
from src.main.exceptions.base_exception import ApplicationException
from src.main.exceptions.unauthorized_exception import UnauthorizedException


def ProcessException(request: Request, exception: Exception) -> JSONResponse:
    """Exception to JSONResponse handler"""
    try:
        raise exception

    except UnauthorizedException:
        print("UnauthorizedException")
        return JSONResponse(status_code=401, content="Unauthorized")

    except AlreadyExistException:
        print("AlreadyExistException")
        return JSONResponse(status_code=400, content="Object Already Exist")

    except ApplicationException:
        print("ERROR")
        return JSONResponse(status_code=500, content="Application Exception")

    except Exception:
        print("ERROR")
        return JSONResponse(status_code=500, content="Internal Server Error")
