import os
from fastapi import Header

from src.main.exceptions.unauthorized_exception import UnauthorizedException


def verify_key(admin_auth: str = Header()):
    if admin_auth != os.environ["ADMIN_AUTH"]:
        raise UnauthorizedException()
