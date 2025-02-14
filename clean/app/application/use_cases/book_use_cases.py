from typing import Optional, List
from app.domain.entities.book import BookCreate, Book
from app.infrastructure.repositories.book_repository import BookRepository

class BookUseCases:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    async def create_book(self, book: BookCreate) -> Book:
        return await self.repository.create(book)

    async def get_book(self, book_id: int) -> Optional[Book]:
        return await self.repository.get_by_id(book_id)

    async def get_all_books(self) -> List[Book]:
        return await self.repository.get_all()

    async def update_book(self, book_id: int, book: BookCreate) -> Optional[Book]:
        return await self.repository.update(book_id, book)

    async def delete_book(self, book_id: int) -> bool:
        return await self.repository.delete(book_id) 