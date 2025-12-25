from fastapi import FastAPI, Depends

app = FastAPI()

async def get_db():
    print("Opening Database Connection")
    db = "THE_DATABASE_OBJECT"
    try:
        yield db
    finally:
        print("Closing Database Connection")

@app.get("/users")
async def list_users(database = Depends(get_db)):
    return {"message": "Using the DB", "db_status": database}