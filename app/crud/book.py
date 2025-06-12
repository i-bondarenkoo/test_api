from app.schemas.book import BookCreate, BookUpdatePatch
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.book import BookOrm
from app.models.author import AuthorOrm
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status


async def create_book_crud(book_in: BookCreate, session: AsyncSession):
    author = await session.get(AuthorOrm, book_in.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    new_book = BookOrm(**book_in.model_dump())
    session.add(new_book)
    await session.commit()
    await session.refresh(new_book)
    return new_book


async def get_list_book_crud(session: AsyncSession, start: int = 0, stop: int = 3):
    stmt = select(BookOrm).order_by(BookOrm.id).offset(start).limit(stop - start)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_book_by_id_crud(book_id: int, session: AsyncSession):
    book = await session.get(BookOrm, book_id)
    return book


async def book_update_crud(book_id: int, book: BookUpdatePatch, session: AsyncSession):
    update_book = await session.get(BookOrm, book_id)
    if not update_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Книга не найдена",
        )
    data = book.model_dump(exclude_unset=True)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Нужно передать данные для обновления",
        )
    for key, value in data.items():
        if value is not None:
            setattr(update_book, key, value)
    await session.commit()
    await session.refresh(update_book)
    return update_book


async def delete_book_crud(book_id: int, session: AsyncSession):
    book = await session.get(BookOrm, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Книга не найдена",
        )
    await session.delete(book)
    await session.commit()
    return {"message": "Книга удалена"}


async def get_book_with_authors_crud(book_id: int, session: AsyncSession):
    stmt = (
        select(BookOrm)
        .where(BookOrm.id == book_id)
        .options(
            selectinload(BookOrm.author),
        )
    )
    result = await session.execute(stmt)
    return result.scalars().first()
