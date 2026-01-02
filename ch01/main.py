from typing import Optional

from fastapi import FastAPI, Depends, status
from fastapi.openapi.models import Response
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


class SearchQuery(BaseModel):
    q: str
    limit: int = 10
    cursor: str | None = None

@app.get("/search/model")
async def search(params: SearchQuery = Depends()):
    return {"query": params.q, "limit": params.limit, "cursor": params.cursor}


class Item(BaseModel):
    id: int
    name: str

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    return Item(id=item_id, name="Sample Item")


class ItemCreate(BaseModel):
    name: str
    price: int
    tags: list[str] = []

@app.post("/items")
def create_item(item: ItemCreate, response: Response):
    response.status_code=status.HTTP_201_CREATED
    response.headers["Location"] = f"/items/1"
    return {"saved": item}
