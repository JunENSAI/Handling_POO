"""
Task:

- Import Header, HTTPException from fastapi.

- Create a dependency function verify_token(token: str = Header(...)).
    - Note: Header(...) tells FastAPI to look for a header named token in the HTTP request.
    - Logic: If token is NOT equal to "supersecret", raise an HTTPException(status_code=400, detail="Invalid Token").
- Create an endpoint GET /secure_data:
    - Inject the dependency: async def secure_data(authorized: bool = Depends(verify_token)).
    - Return {"message": "Welcome to the secret area"}.
"""

from fastapi import Header, HTTPException, FastAPI, Depends

app = FastAPI()

async def verify_token(token:str=Header()):
    if token != "supersecret":
        raise HTTPException(status_code=400, detail="Invalid Token")
    return True

@app.get("/secure_data")
async def secure_data(authorized: bool = Depends(verify_token)):
    return {"message": "Welcome to the secret area"}