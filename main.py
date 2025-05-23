from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
class Item(BaseModel):
    id: int
    name: str
    description: str
    
items_db = []
@app.get("/items/", response_model=list[Item])
def get_items():
    return items_db

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if any(existing_item.id == item.id for existing_item in items_db):
        raise HTTPException(status_code=400, detail="Item já existente.")
    items_db.append(item)
    return item



