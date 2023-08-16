from typing import Optional

from pydantic import BaseModel, ConfigDict, model_serializer


class Category(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    resume_value: Optional[float] = None

    @model_serializer
    def ser_model(self) -> str:
        return f"{self.name.capitalize()}: ${self.resume_value}"


class ListCategories(BaseModel):
    categories: list[Category] = []
