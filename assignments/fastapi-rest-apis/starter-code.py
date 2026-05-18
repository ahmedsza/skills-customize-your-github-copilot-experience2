from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Items API", description="A simple REST API built with FastAPI")

# --- Sample data ---
items = [
    {"id": 1, "name": "Book", "price": 12.99, "in_stock": True},
    {"id": 2, "name": "Pen", "price": 1.49, "in_stock": True},
    {"id": 3, "name": "Backpack", "price": 34.99, "in_stock": False},
]


# --- Pydantic model ---
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool


# --- Task 1: Root and list endpoints ---

@app.get("/")
def read_root():
    # TODO: Return a welcome message
    pass


@app.get("/items")
def get_items(q: Optional[str] = None):
    # TODO: Return the list of items
    # TODO: If 'q' is provided, filter items whose name contains 'q' (case-insensitive)
    pass


# --- Task 2: Path parameters ---

@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: Find and return the item with the given item_id
    # TODO: Raise HTTPException with status 404 if not found
    pass


# --- Task 3: POST endpoint ---

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    # TODO: Assign a new id to the item (max existing id + 1)
    # TODO: Append the item to the items list and return it
    pass
