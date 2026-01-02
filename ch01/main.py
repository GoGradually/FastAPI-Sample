from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/search")
async def search(q: str, limit: int = 10, cursor: Optional[str] = None):
    return {"query": q, "limit": limit, "cursor": cursor}

class ItemCreate(BaseModel):
    name: str
    price: int
    tags: list[str] = []

@app.post("/items")
def create_item(item: ItemCreate):
    return {"saved": item}