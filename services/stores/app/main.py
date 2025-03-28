from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/stores")
async def books():
    books = [
        {"id":1 ,"name": "Sucursal 1", "location":"Av. Ayacucho #5555"},
        {"id":2 ,"name": "Sucursal 2", "location":"Av. América #5555"},
        {"id":3 ,"name": "Sucursal 3", "location":"Av. Circunvalación #5555"},
    ]

    return books
