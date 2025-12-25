"""
Task:

- Create a model Product:
    - name (str)
    - price (float)
    - in_stock (bool, default is True)

- Create an endpoint POST /create_product:
    - Accepts a item: Product.
    - Logic:
        - Calculate the tax (20% of price).
        - Return a dictionary: {"name": item.name, "price_with_tax": item.price * 1.2, "status": item.in_stock}.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/create_product")
async def create_product(item: Product):
    return {"name": item.name, "price_with_tax": item.price * 1.2, "status": item.in_stock}