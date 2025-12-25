from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInDB:
    def __init__(self):
        self.username = "alice"
        self.email = "alice@example.com"
        self.password = "secret_hash_123" # just imagine hh

class UserPublic(BaseModel):
    username: str
    email: str
    
    class Config:
        from_attributes = True

@app.get("/me", response_model=UserPublic)
async def read_current_user():
    user = UserInDB() 
    return user