"""
Task:

- Define a class FakeUserDB with attributes: username, full_name, credit_card_number.

- Define a Pydantic model UserProfile that ONLY includes username and full_name. (Enable from_attributes = True inside Config).

- Create an endpoint GET /profile:
    - Declare response_model=UserProfile.
    - Instantiate a FakeUserDB with a fake credit card number.
    - Return the object.

- Goal: Prove that the credit card number is NOT in the output.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FakeUserDB:
    def __init__(self):
        self.username = "devTo"
        self.email = "devto@example.com"
        self.credit_card_number = "467862137412456" # imagine ahhh

class UserProfile(BaseModel):
    username: str
    email: str
    
    class Config:
        from_attributes = True

@app.get("/profile", response_model=UserProfile)
async def read_current_user():
    db_user = FakeUserDB() 
    return db_user