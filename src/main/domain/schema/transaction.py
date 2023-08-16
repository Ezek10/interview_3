from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, model_serializer

from src.main.domain.schema.account import Account
from src.main.domain.schema.category import Category


class Transaction(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    amount: int
    description: Optional[str] = None
    created_at: datetime
    category: Category
    account: Account

    @model_serializer
    def ser_model(self) -> str:
        if self.description is None:
            return f"{self.id} - ${self.amount} - {self.category.name} - {self.account.name} - {self.created_at}"
        return f"{self.id} - ${self.amount} - {self.description} - {self.category.name} - {self.account.name} - {self.created_at}"


class ListTransactions(BaseModel):
    transactions: list[Transaction] = []
