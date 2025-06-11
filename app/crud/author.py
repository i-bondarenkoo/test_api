from fastapi import HTTPException, status
from app.schemas.author import CreateAuthor
from app.models.author import AuthorOrm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload


async def create_author_crud(author_in: CreateAuthor, session: AsyncSession):
    new_author = AuthorOrm(**author_in.model_dump())
    session.add(new_author)
    await session.commit()
    await session.refresh(new_author)
    return new_author


async def get_list_authors_crud(session: AsyncSession, start: int = 0, stop: int = 3):
    stmt = select(AuthorOrm).order_by(AuthorOrm.id).offset(start).limit(stop - start)
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_author_by_id_crud(author_id: int, session: AsyncSession):
    author = await session.get(AuthorOrm, author_id)
    return author


async def delete_author_crud(author_id: int, session: AsyncSession):
    current_author = await session.get(AuthorOrm, author_id)
    if not current_author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Автор не найден",
        )
    await session.delete(current_author)
    await session.commit()
    return {"message": "Автор удален"}


async def get_authors_with_more_books_crud(author_id: int, session: AsyncSession):
    author = await session.get(AuthorOrm, author_id)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Автор не найден",
        )
    stmt = (
        select(AuthorOrm)
        .where(AuthorOrm.id == author_id)
        .options(selectinload(AuthorOrm.books))
    )
    result = await session.execute(stmt)
    return result.scalars().first()
