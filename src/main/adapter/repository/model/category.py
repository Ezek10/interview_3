from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from src.main.adapter.repository.config import Base


class CategoryDB(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    user_id = Column(String(50), ForeignKey("user.id"), nullable=False)

    transactions: Mapped["TransactionDB"] = relationship(back_populates="category")

    def __str__(self):
        return f"CategoryDB({self.user_id} - {self.id} - {self.name})"

    def __repr__(self):
        return self.__str__()
