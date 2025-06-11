from app.schemas.author import CreateAuthor, AuthorResponse, AuthorResponseWithOutID
from app.schemas.book import (
    BookCreate,
    BookResponse,
    BookUpdatePatch,
    BookResponseWithRelationship,
)

BookResponseWithRelationship.model_rebuild()
