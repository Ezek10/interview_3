from datetime import datetime

from pydantic import Field
from sqlalchemy import Column, DateTime, Integer, String

from src.main.repository.config import Base


class CarrerDB(Base):
    __tablename__ = "carrer"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    create_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(
        sa_column=Column(
            DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
        )
    )

    def __repr__(self):
        return f"CarrerDB({self.id})"
