from datetime import datetime

from pydantic import Field
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship
from src.main.repository.config import Base


class CarrerRegistrationDB(Base):
    __tablename__ = "carrer_registration"

    id = Column(Integer, primary_key=True, nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"), nullable=False)
    carrer_id = Column(Integer, ForeignKey("carrer.id"), nullable=False)
    registration_year = Column(Integer, nullable=False)
    create_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(
        sa_column=Column(
            DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
        )
    )

    person: Mapped["PersonDB"] = relationship(back_populates="carrers")

    def __repr__(self):
        return f"CarrerRegistrationDB({self.id})"
