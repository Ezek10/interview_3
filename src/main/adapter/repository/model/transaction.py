from datetime import datetime

from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from src.main.adapter.repository.config import Base


class TransactionDB(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    account_id = Column(Integer, ForeignKey("account.id"), nullable=False)
    user_id = Column(String(50), ForeignKey("user.id"), nullable=False)
    description = Column(String(50), nullable=True)
    created_at = Column(Date, default=datetime.now())

    category: Mapped["CategoryDB"] = relationship(back_populates="transactions")
    account: Mapped["AccountDB"] = relationship(back_populates="transactions")

    def __str__(self):
        return f"TransactionDB({self.user_id} - {self.id} - {self.amount} - {self.category} - {self.account})"

    def __repr__(self):
        return self.__str__()
