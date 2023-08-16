from functools import wraps

from fastapi.datastructures import Headers
from fastapi.responses import JSONResponse


def AdminAuthorization(controller):
    """To use this Decorator add a "request: fastapi.Request"
    in the function to read the requests headers
    """

    @wraps(controller)
    async def auth(*args, **kwargs):
        headers: Headers = kwargs["request"].headers
        if "1234" in headers.get("admin-auth"):
            return await controller(*args, **kwargs)
        else:
            return JSONResponse(
                status_code=403, content="Unauthorized for this operation"
            )

    return auth
