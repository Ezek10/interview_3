from src.main.exceptions.base_exception import ApplicationException


class AlreadyExistException(ApplicationException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
