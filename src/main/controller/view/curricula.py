from pydantic import BaseModel, ConfigDict, Field, RootModel


class Curricula(BaseModel):
    model_config = ConfigDict(from_attributes=True, str_to_lower=True)

    carrer_id: int = Field(ge=1)
    subjects_ids: list[int]


class Curriculas(RootModel):
    root: list[Curricula]

    def __iter__(self):
        return iter(self.root)
