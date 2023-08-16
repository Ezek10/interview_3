from datetime import datetime

from sqlalchemy import Column, Date, String

from src.main.adapter.repository.config import Base


class UserDB(Base):
    __tablename__ = "user"

    id = Column(String(50), primary_key=True)  # phone
    email = Column(String(50), unique=True)
    name = Column(String(20), nullable=True)
    created_at = Column(Date, default=datetime.now())
    updated_at = Column(Date, default=datetime.now(), onupdate=datetime.now())

    def __str__(self):
        return f"UserDB({self.id} - {self.email} - {self.name} - {self.created_at} - {self.updated_at})"

    def __repr__(self):
        return self.__str__()
