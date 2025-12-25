"""
Task:
- Create an endpoint GET /add/{x}/{y}:

    - Takes two parameters x and y.
    - Returns a dictionary related from operation on x and y .

- Create an endpoint GET /square/{number}:
    - Takes number (float).
    - Returns the operation of number to square.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/add/{x}/{y}")
async def add(x:float, y:float):
    return {"operation": "add", "result": x + y}

@app.get("/square/{number}")
async def square(number:float):
    return {"operation": "square", "result": number * number}