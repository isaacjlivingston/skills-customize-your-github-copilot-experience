# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    price: float = Field(..., ge=0)


# In-memory data store for assignment purposes
items = [
    {"id": 1, "name": "Pencil", "price": 0.99},
    {"id": 2, "name": "Eraser", "price": 1.49},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return {"items": items}


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    # TODO: Prevent duplicate IDs before appending.
    items.append(item.model_dump())
    return {"message": "Item created", "item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    # TODO: Find and replace the item matching item_id.
    raise HTTPException(status_code=501, detail="Not implemented yet")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: Remove the item matching item_id.
    raise HTTPException(status_code=501, detail="Not implemented yet")


# Run locally with:
# uvicorn starter-code:app --reload
