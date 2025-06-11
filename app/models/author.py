from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.book import BookOrm


class AuthorOrm(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    birth_year: Mapped[int] = mapped_column(Integer, nullable=False)

    # связи
    books: Mapped[list["BookOrm"]] = relationship(
        "BookOrm", back_populates="author", cascade="all, delete-orphan"
    )
