from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")
Y = TypeVar("Y")


class ResponseSchema(BaseModel, Generic[T]):
    """basic response for any request"""

    detail: str
    result: Optional[T] = None


class PageResponse(BaseModel, Generic[Y]):
    """The response for a pagination query."""

    page_number: int
    page_size: int
    total_pages: int
    total_record: int
    content: Y

    def __eq__(self, __value: object) -> bool:
        if type(__value) is not PageResponse:
            raise TypeError()
        return self.model_dump() == __value.model_dump()
