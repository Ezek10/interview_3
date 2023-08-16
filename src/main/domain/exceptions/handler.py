from fastapi import Request
from fastapi.responses import JSONResponse

from src.main.domain.exceptions.account_not_found import AccountNotFound
from src.main.domain.exceptions.base_exception import \
    ApplicationException
from src.main.domain.exceptions.category_not_found import CategoryNotFound


def ProcessException(request: Request, exception: Exception) -> JSONResponse:
    try:
        raise exception

    except CategoryNotFound as exc:
        print("ERROR")
        return JSONResponse(status_code=404, content=exc.args)

    except AccountNotFound as exc:
        print("ERROR")
        return JSONResponse(status_code=404, content=exc.args)

    except ApplicationException:
        print("ERROR")
        return JSONResponse(status_code=500, content="Application Exception")

    except Exception:
        print("ERROR")
        return JSONResponse(status_code=500, content="Internal Server Error")
