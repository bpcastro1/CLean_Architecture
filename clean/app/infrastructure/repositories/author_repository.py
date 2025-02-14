from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.entities.author import Author, AuthorCreate
from app.infrastructure.database.models import Author as AuthorModel
from app.domain.repositories.base_repository import BaseRepository

class AuthorRepository(BaseRepository[Author]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, author: AuthorCreate) -> Author:
        db_author = AuthorModel(
            name=author.name,
            biography=author.biography
        )
        self.session.add(db_author)
        await self.session.commit()
        await self.session.refresh(db_author)
        return Author.from_orm(db_author)

    async def get_by_id(self, id: int) -> Optional[Author]:
        result = await self.session.execute(
            select(AuthorModel).filter(AuthorModel.id == id)
        )
        db_author = result.scalar_one_or_none()
        if db_author is None:
            return None
        return Author.from_orm(db_author)

    async def get_all(self) -> List[Author]:
        result = await self.session.execute(select(AuthorModel))
        return [Author.from_orm(author) for author in result.scalars().all()]

    async def update(self, id: int, author: AuthorCreate) -> Optional[Author]:
        db_author = await self.get_by_id(id)
        if db_author is None:
            return None
        
        update_data = author.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_author, key, value)
        
        await self.session.commit()
        await self.session.refresh(db_author)
        return Author.from_orm(db_author)

    async def delete(self, id: int) -> bool:
        result = await self.session.execute(
            select(AuthorModel).filter(AuthorModel.id == id)
        )
        db_author = result.scalar_one_or_none()
        if db_author is None:
            return False
        
        await self.session.delete(db_author)
        await self.session.commit()
        return True 