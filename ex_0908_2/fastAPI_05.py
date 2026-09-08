from fastapi import FastAPI
from pydantic import BaseModel

# post 요청

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    return item


