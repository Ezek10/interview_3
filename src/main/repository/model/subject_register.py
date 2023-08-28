from datetime import datetime

from pydantic import Field
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship
from src.main.repository.config import Base


class SubjectRegistrationDB(Base):
    __tablename__ = "subject_registration"

    id = Column(Integer, primary_key=True, nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)
    attempt = Column(Integer, nullable=False)

    create_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(
        sa_column=Column(
            DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
        )
    )

    person: Mapped["PersonDB"] = relationship(back_populates="subjects")

    def __repr__(self):
        return f"SubjectRegistrationDB({self.id})"
