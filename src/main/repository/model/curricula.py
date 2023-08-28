from sqlalchemy import Column, ForeignKey, Integer

from src.main.repository.config import Base


class CurriculaDB(Base):
    __tablename__ = "curricula"

    carrer_id = Column(
        Integer, ForeignKey("carrer.id"), nullable=False, primary_key=True
    )
    subject_id = Column(
        Integer, ForeignKey("subject.id"), nullable=False, primary_key=True
    )

    def __repr__(self):
        return f"CurriculaDB({self.carrer_id})"
