from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.entities.book import Book, BookCreate
from app.infrastructure.database.models import Book as BookModel
from app.domain.repositories.base_repository import BaseRepository

class BookRepository(BaseRepository[Book]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, book: BookCreate) -> Book:
        db_book = BookModel(
            title=book.title,
            description=book.description,
            publication_year=book.publication_year,
            author_id=book.author_id
        )
        self.session.add(db_book)
        await self.session.commit()
        await self.session.refresh(db_book)
        return Book.from_orm(db_book)

    async def get_by_id(self, id: int) -> Optional[Book]:
        result = await self.session.execute(
            select(BookModel).filter(BookModel.id == id)
        )
        db_book = result.scalar_one_or_none()
        if db_book is None:
            return None
        return Book.from_orm(db_book)

    async def get_all(self) -> List[Book]:
        result = await self.session.execute(select(BookModel))
        return [Book.from_orm(book) for book in result.scalars().all()]

    async def update(self, id: int, book: BookCreate) -> Optional[Book]:
        db_book = await self.get_by_id(id)
        if db_book is None:
            return None
        
        update_data = book.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_book, key, value)
        
        await self.session.commit()
        await self.session.refresh(db_book)
        return Book.from_orm(db_book)

    async def delete(self, id: int) -> bool:
        result = await self.session.execute(
            select(BookModel).filter(BookModel.id == id)
        )
        db_book = result.scalar_one_or_none()
        if db_book is None:
            return False
        
        await self.session.delete(db_book)
        await self.session.commit()
        return True 