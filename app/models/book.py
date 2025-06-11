from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.author import AuthorOrm


class BookOrm(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(35), nullable=False)
    published_year: Mapped[int] = mapped_column(Integer, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE"))

    # связи
    author: Mapped["AuthorOrm"] = relationship("AuthorOrm", back_populates="books")
