from app.schemas.author import (
    CreateAuthor,
    AuthorResponse,
    AuthorResponseWithOutID,
    AuthorResponsewithBooks,
)
from app.schemas.book import (
    BookCreate,
    BookResponse,
    BookUpdatePatch,
    BookResponseWithRelationship,
    BookResponseWithOutID,
)

BookResponseWithRelationship.model_rebuild()
AuthorResponsewithBooks.model_rebuild()
