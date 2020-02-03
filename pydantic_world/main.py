# from https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Foo(BaseModel):
    param1: str
    param2: str
    default_param: str = "FooBar"

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/")
async def test_pydantic_classes(hello: Foo):
    return hello

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}