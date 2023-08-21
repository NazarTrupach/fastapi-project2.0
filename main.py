from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}


# Path parameters
@app.get("/get-item/{item_id}/")
def get_item(item_id: int = Path(..., description="The Api for your gods", gt=0, le=5)):
    return inventory[item_id]


# Query Parameters
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data": "Not found"}