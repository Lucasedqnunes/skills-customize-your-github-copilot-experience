from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str

items = []

@app.get("/items")
def list_items() -> List[dict]:
    return [{"id": i+1, "name": item["name"]} for i, item in enumerate(items)]

@app.post("/items", status_code=201)
def add_item(item: Item):
    items.append(item.dict())
    return {"id": len(items), "name": item.name}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if 1 <= item_id <= len(items):
        item = items[item_id-1]
        return {"id": item_id, "name": item["name"]}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if 1 <= item_id <= len(items):
        items.pop(item_id-1)
        return
    raise HTTPException(status_code=404, detail="Item not found")
