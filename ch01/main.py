from typing import Optional

from fastapi import FastAPI

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