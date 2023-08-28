import os

import pytest
from src.main.authorization.admin import verify_key
from src.main.exceptions.unauthorized_exception import UnauthorizedException


def test_verify_key_not_ok():
    os.environ["ADMIN_AUTH"] = "auth"
    with pytest.raises(UnauthorizedException):
        verify_key("not auth")


def test_verify_key_ok():
    os.environ["ADMIN_AUTH"] = "auth"
    verify_key("auth")
    assert True
