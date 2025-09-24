from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Arc Raiders Items API")

# Example Item Model
class Item(BaseModel):
    name: str
    category: str
    description: str = None

# The full items list (add all your items here)
items = [
    {"name": "Anvil I", "category": "Weapon", "description": "Single-action hand cannon with high damage."},
    {"name": "Arpeggio I", "category": "Weapon", "description": "3-round burst assault rifle."},
    {"name": "Adrenaline Shot", "category": "Medical", "description": "Boosts energy and health."},
    {"name": "ARC Alloy", "category": "Material", "description": "Specialized alloys from ARC technology."},
    # Add all remaining items here...
]

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Arc Raiders Items API"}

# Endpoint to get all items
@app.get("/items", response_model=List[Item])
def get_items():
    return items

# Endpoint to filter items by category
@app.get("/items/{category}", response_model=List[Item])
def get_items_by_category(category: str):
    filtered_items = [item for item in items if item["category"].lower() == category.lower()]
    return filtered_items
