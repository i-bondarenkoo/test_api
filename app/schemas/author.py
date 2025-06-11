from pydantic import BaseModel, ConfigDict


class CreateAuthor(BaseModel):
    first_name: str
    last_name: str
    birth_year: int


class AuthorResponse(CreateAuthor):
    id: int

    model_config = ConfigDict(from_attributes=True)


class AuthorResponseWithOutID(CreateAuthor):

    model_config = ConfigDict(from_attributes=True)
