from fastapi import APIRouter, Body, Depends, Query, HTTPException, status, Path
from app.schemas.author import CreateAuthor, AuthorResponse, AuthorResponsewithBooks
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app import crud
from app.core.database import get_session_with_db

router = APIRouter(
    prefix="/authors",
    tags=["Author"],
)


@router.post("/", response_model=AuthorResponse)
async def create_author(
    author_in: Annotated[
        CreateAuthor, Body(description="Поля для создания объекта в БД")
    ],
    session: AsyncSession = Depends(get_session_with_db),
):
    return await crud.create_author_crud(author_in=author_in, session=session)


@router.get("/", response_model=list[AuthorResponse])
async def get_list_authors(
    start: int = Query(ge=0, description="Начальный индекс списка авторов"),
    stop: int = Query(gt=0, description="Конечный индекс списка авторов"),
    session: AsyncSession = Depends(get_session_with_db),
):
    if start > stop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Некорректные значения индексов списка",
        )
    # response = await crud.get_list_authors_crud(session=session, start=start, stop=stop)
    # if response == []:
    #     return f"К сожалению, список авторов пуст"
    # return response
    return await crud.get_list_authors_crud(session=session, start=start, stop=stop)


@router.get("/{author_id}", response_model=AuthorResponse)
async def get_author_by_id(
    author_id: Annotated[
        int, Path(gt=0, description="ID Автора, для получения детальной информации")
    ],
    session: AsyncSession = Depends(get_session_with_db),
):
    author = await crud.get_author_by_id_crud(author_id=author_id, session=session)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Такого автора нет в списке",
        )
    return author


@router.delete("/{author_id}")
async def delete_author(
    author_id: Annotated[
        int, Path(gt=0, description="ID автора, которого нужно удалить")
    ],
    session: AsyncSession = Depends(get_session_with_db),
):
    return await crud.delete_author_crud(author_id=author_id, session=session)


@router.get("/{author_id}/books", response_model=AuthorResponsewithBooks)
async def get_author_with_more_books(
    author_id: Annotated[
        int, Path(gt=0, description="ID Автора для вывода дополнительной информации")
    ],
    session: AsyncSession = Depends(get_session_with_db),
):
    return await crud.get_authors_with_more_books_crud(
        author_id=author_id, session=session
    )
