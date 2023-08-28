from pydantic import BaseModel, ConfigDict, Field, RootModel


class Carrer(BaseModel):
    model_config = ConfigDict(from_attributes=True, str_to_lower=True)

    id: int = Field(ge=1)
    name: str


class Carrers(RootModel):
    root: list[Carrer]

    def __iter__(self):
        return iter(self.root)
