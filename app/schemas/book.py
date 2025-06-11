from pydantic import BaseModel, ConfigDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.schemas.author import AuthorResponseWithOutID


class BookCreate(BaseModel):
    title: str
    published_year: int
    author_id: int


class BookResponse(BookCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookResponseWithOutID(BaseModel):
    title: str
    published_year: int


class BookUpdatePatch(BaseModel):
    title: str | None = None
    published_year: int | None = None
    author_id: int | None = None


class BookResponseWithRelationship(BaseModel):
    title: str
    published_year: int
    author: "AuthorResponseWithOutID"
