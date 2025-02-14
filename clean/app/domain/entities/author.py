from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class AuthorBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    biography: Optional[str] = Field(None, max_length=500)

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 