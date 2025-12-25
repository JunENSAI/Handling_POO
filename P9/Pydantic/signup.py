from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: str
    age: int


@app.post("/signup")
async def create_user(user: UserSignup):
    
    if user.age < 18:
        return {"error": "You must be 18+"}
        
    return {
        "message": "User created successfully",
        "username": user.username,
        "sent_email_to": user.email
    }