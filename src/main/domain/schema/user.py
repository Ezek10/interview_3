from typing import Optional

from pydantic import BaseModel, ConfigDict, model_serializer


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    phone: str
    email: Optional[str] = None
    name: Optional[str] = ""

    @model_serializer
    def ser_model(self) -> str:
        return f"{self.name.capitalize()} {self.phone} {self.email}"


class ListUsers(BaseModel):
    users: list[User] = []
