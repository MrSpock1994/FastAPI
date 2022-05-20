from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(min_length=1, max_length=100, 
                        title="Description of the book")
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "af2db729-ae20-425c-a55f-d67ed1658ec7",
                "title": "Computer science",
                "author": "Coding",
                "Description": "Nothing",
                "rating": 75
            }
        }


BOOKS = []



@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()
    
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books =[]
        while i <= books_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books
    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x



@app.post("/")
async def create(book: Book):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]


@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0
    for x in BOOKS:
        counter += 1
        #new_books = []
        if x.id == book_id:
            BOOKS.pop(counter - 1)
            return BOOKS


def create_books_no_api():
    book_1 = Book(id="a254f76a-4fe1-4d06-b75c-488f13a1a12f",
                title="Title 1",
                author="Author 1",
                description="Description 1",
                rating=34)
    book_2 = Book(id="af494109-9c2c-4383-9da6-05113138c0f4",
                title="Title 2",
                author="Author 2",
                description="Description 2",
                rating=54) 
    book_3 = Book(id="551861cd-d95a-4ea2-9183-a700fff484b0",
                title="Title 3",
                author="Author 3",
                description="Description 3",
                rating=75) 
    book_4 = Book(id="eb3af0bf-b386-4973-912a-7e5ef6c26cff",
                title="Title 4",
                author="Author 4",
                description="Description 4",
                rating=99)    
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)    