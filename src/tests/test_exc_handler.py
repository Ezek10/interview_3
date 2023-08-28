from src.main.exceptions.already_exist_exception import AlreadyExistException
from src.main.exceptions.base_exception import ApplicationException
from src.main.exceptions.handler import ProcessException
from src.main.exceptions.unauthorized_exception import UnauthorizedException


def test_handler_unauthorized_exc():
    exception = UnauthorizedException
    response = ProcessException(request=None, exception=exception)
    assert response.status_code == 401


def test_handler_already_exist_exc():
    exception = AlreadyExistException
    response = ProcessException(request=None, exception=exception)
    assert response.status_code == 400


def test_handler_base_exc():
    exception = ApplicationException
    response = ProcessException(request=None, exception=exception)
    assert response.status_code == 500


def test_handler_another_exc():
    exception = Exception
    response = ProcessException(request=None, exception=exception)
    assert response.status_code == 500
