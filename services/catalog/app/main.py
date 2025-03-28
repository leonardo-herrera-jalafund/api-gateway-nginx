from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/books")
async def books():
    books = [
        {"id":1 ,"name": "Pedro Páramo", "author":"Juan Rulfo"},
        {"id":2 ,"name": "Raza de Bronce", "author":"Alcides Arguedas"},
        {"id":3 ,"name": "La casa junto al rio", "author":"Elena Garro"},
    ]

    return books

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    books = [
        {"id":1 ,"name": "Pedro Páramo", "author":"Juan Rulfo", "price": 320, "existence": 9},
        {"id":2 ,"name": "Raza de Bronce", "author":"Alcides Arguedas", "price": 300, "existence": 6},
        {"id":3 ,"name": "La casa junto al rio", "author":"Elena Garro", "price": 410, "existence": 10},
    ]

    result = next((sub for sub in books if sub['id'] == book_id), None)
    return result