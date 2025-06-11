from fastapi import APIRouter, Body, HTTPException, status, Depends, Query, Path
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session_with_db
from app.schemas.book import (
    BookCreate,
    BookResponse,
    BookUpdatePatch,
    BookResponseWithRelationship,
)
from app import crud
from typing import Annotated

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.post("/", response_model=BookResponse)
async def create_book(
    book_in: Annotated[
        BookCreate, Body(description="Поля объекта для сохранения в БД")
    ],
    session: AsyncSession = Depends(get_session_with_db),
):
    check_author = await crud.get_author_by_id_crud(
        author_id=book_in.author_id, session=session
    )
    if not check_author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Такого автора нет в списке",
        )
    return await crud.create_book_crud(book_in=book_in, session=session)


@router.get("/", response_model=list[BookResponse])
async def get_list_book(
    session: AsyncSession = Depends(get_session_with_db),
    start: int = Query(0, ge=0, description="Начальный индекс списка книг"),
    stop: int = Query(3, gt=0, description="Начальный индекс списка книг"),
):
    if start > stop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Введены некорректные индексы списка",
        )
    return await crud.get_list_book_crud(start=start, session=session, stop=stop)


@router.get("/{book_id}", response_model=BookResponse)
async def get_book_by_id(
    book_id: Annotated[int, Path(description="Индекс книги в БД")],
    session: AsyncSession = Depends(get_session_with_db),
):
    book = await crud.get_book_by_id_crud(book_id=book_id, session=session)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Книга не найдена",
        )
    return book


@router.patch("/{book_id}", response_model=BookResponse)
async def book_update(
    book_id: Annotated[
        int, Path(gt=0, description="ID объекта, который будем обновлять")
    ],
    book: Annotated[BookUpdatePatch, Body(description="Заполните поля для обновления")],
    session: AsyncSession = Depends(get_session_with_db),
):
    return await crud.book_update_crud(
        book_id=book_id,
        book=book,
        session=session,
    )


@router.delete("/{book_id}")
async def delete_book(
    book_id: Annotated[int, Path(gt=0, description="ID книги, которую нужно удалить")],
    session: AsyncSession = Depends(get_session_with_db),
):
    return await crud.delete_book_crud(book_id=book_id, session=session)


@router.get("/{book_id}/authors", response_model=BookResponseWithRelationship)
async def get_book_with_authors(
    book_id: Annotated[
        int, Path(gt=0, description="ID Книги для получения дополнительной информации")
    ],
    session: AsyncSession = Depends(get_session_with_db),
):
    return await crud.get_book_with_authors_crud(book_id=book_id, session=session)
