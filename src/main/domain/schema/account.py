from typing import Optional

from pydantic import BaseModel, ConfigDict, model_serializer


class Account(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    currency: Optional[str] = ""
    resume_value: Optional[float] = None

    @model_serializer
    def ser_model(self) -> str:
        return f"{self.name.capitalize()}: {self.currency.upper()}$ {self.resume_value}"


class ListAccounts(BaseModel):
    accounts: list[Account] = []
