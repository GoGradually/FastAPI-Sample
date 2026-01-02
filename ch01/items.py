from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_items():
    return ["a", "b"]

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
