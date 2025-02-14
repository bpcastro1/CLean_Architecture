from typing import Optional, List
from app.domain.entities.author import AuthorCreate, Author
from app.infrastructure.repositories.author_repository import AuthorRepository

class AuthorUseCases:
    def __init__(self, repository: AuthorRepository):
        self.repository = repository

    async def create_author(self, author: AuthorCreate) -> Author:
        return await self.repository.create(author)

    async def get_author(self, author_id: int) -> Optional[Author]:
        return await self.repository.get_by_id(author_id)

    async def get_all_authors(self) -> List[Author]:
        return await self.repository.get_all()

    async def update_author(self, author_id: int, author: AuthorCreate) -> Optional[Author]:
        return await self.repository.update(author_id, author)

    async def delete_author(self, author_id: int) -> bool:
        return await self.repository.delete(author_id) 