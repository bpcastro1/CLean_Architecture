from fastapi import APIRouter, Depends, HTTPException
from app.domain.entities.author import AuthorCreate, Author
from app.domain.entities.book import BookCreate, Book
from app.application.use_cases.author_use_cases import AuthorUseCases
from app.application.use_cases.book_use_cases import BookUseCases
from .dependencies import get_author_use_cases, get_book_use_cases
from typing import List

router = APIRouter()

@router.post("/authors", response_model=Author)
async def create_author(
    author: AuthorCreate,
    use_cases: AuthorUseCases = Depends(get_author_use_cases)
):
    return await use_cases.create_author(author)

@router.get("/authors/{author_id}", response_model=Author)
async def get_author(
    author_id: int,
    use_cases: AuthorUseCases = Depends(get_author_use_cases)
):
    author = await use_cases.get_author(author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.post("/books", response_model=Book)
async def create_book(
    book: BookCreate,
    use_cases: BookUseCases = Depends(get_book_use_cases)
):
    return await use_cases.create_book(book)

@router.get("/books/{book_id}", response_model=Book)
async def get_book(
    book_id: int,
    use_cases: BookUseCases = Depends(get_book_use_cases)
):
    book = await use_cases.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book 