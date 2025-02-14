from app.infrastructure.database.database import get_db
from app.infrastructure.repositories.author_repository import AuthorRepository
from app.infrastructure.repositories.book_repository import BookRepository
from app.application.use_cases.author_use_cases import AuthorUseCases
from app.application.use_cases.book_use_cases import BookUseCases
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

async def get_author_repository(session: AsyncSession = Depends(get_db)) -> AuthorRepository:
    return AuthorRepository(session)

async def get_book_repository(session: AsyncSession = Depends(get_db)) -> BookRepository:
    return BookRepository(session)

async def get_author_use_cases(
    repository: AuthorRepository = Depends(get_author_repository)
) -> AuthorUseCases:
    return AuthorUseCases(repository)

async def get_book_use_cases(
    repository: BookRepository = Depends(get_book_repository)
) -> BookUseCases:
    return BookUseCases(repository) 