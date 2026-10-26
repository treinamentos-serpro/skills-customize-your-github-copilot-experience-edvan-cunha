from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book API")


class BookInput(BaseModel):
    title: str
    author: str
    year: int


books = [
    {"id": 1, "title": "Frankenstein", "author": "Mary Shelley", "year": 1818},
    {"id": 2, "title": "The Left Hand of Darkness", "author": "Ursula K. Le Guin", "year": 1969},
]