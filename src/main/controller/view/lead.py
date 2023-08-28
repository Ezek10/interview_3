from abc import ABC
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field, RootModel


class Person(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    email: EmailStr
    address: str
    phone: str


class SubjectRegistration(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    subject_id: int = Field(ge=1)
    attempt: int = Field(ge=1)


class CarrerRegistration(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    carrer_id: int = Field(ge=1)
    registration_year: int = Field(gt=1950, le=datetime.now().year)


class Lead(BaseModel, ABC):
    person: Person
    subjects: list[SubjectRegistration]
    carrers: list[CarrerRegistration]


class CreateLead(Lead):
    pass


class CreateLeads(RootModel):
    root: list[CreateLead]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]


class GetLead(Lead):
    model_config = ConfigDict(from_attributes=True)
    id: int


class GetLeads(RootModel):
    root: list[GetLead]

    def __iter__(self):
        return iter(self.root)
