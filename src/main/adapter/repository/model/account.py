from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from src.main.adapter.repository.config import Base


class AccountDB(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    currency = Column(String(5), nullable=True)
    user_id = Column(String(50), ForeignKey("user.id"), nullable=False)

    transactions: Mapped["TransactionDB"] = relationship(back_populates="account")

    def __str__(self):
        return f"AccountDB({self.user_id} - {self.id} - {self.name} - {self.currency})"

    def __repr__(self):
        return self.__str__()
