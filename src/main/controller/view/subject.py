from pydantic import BaseModel, ConfigDict, Field, RootModel


class Subject(BaseModel):
    model_config = ConfigDict(from_attributes=True, str_to_lower=True)

    id: int = Field(ge=1)
    name: str


class Subjects(RootModel):
    root: list[Subject]

    def __iter__(self):
        return iter(self.root)
