from datetime import datetime

from pydantic import Field
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import Relationship, Mapped

from src.main.repository.config import Base


class PersonDB(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    address = Column(String)
    phone = Column(String)
    create_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(
        sa_column=Column(
            DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
        )
    )

    carrers: Mapped[list["CarrerRegistrationDB"]] = Relationship(
        back_populates="person"
    )
    subjects: Mapped[list["SubjectRegistrationDB"]] = Relationship(
        back_populates="person"
    )

    def __repr__(self):
        return f"PersonDB({self.id})"
