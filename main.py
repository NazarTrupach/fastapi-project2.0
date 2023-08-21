from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {}


# Path parameters
@app.get("/get-item/{item_id}/")
async def get_item(item_id: int = Path(..., description="The Api for your gods", gt=0)):
    return inventory[item_id]


# Query Parameters
@app.get("/get-by-name")
async def get_item(name: str = Query(title="Name", description="Name of item")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}


# Request body and Post method
@app.post("/create-item{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"error": "Item ID already exist!"}

    inventory[item_id] = item
    return inventory[item_id]

