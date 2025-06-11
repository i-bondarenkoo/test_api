from pydantic import BaseModel, ConfigDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.schemas.book import BookResponseWithOutID


class CreateAuthor(BaseModel):
    first_name: str
    last_name: str
    birth_year: int


class AuthorResponse(CreateAuthor):
    id: int

    model_config = ConfigDict(from_attributes=True)


class AuthorResponseWithOutID(CreateAuthor):

    model_config = ConfigDict(from_attributes=True)


class AuthorResponsewithBooks(BaseModel):
    first_name: str
    last_name: str
    birth_year: int
    books: list["BookResponseWithOutID"]
