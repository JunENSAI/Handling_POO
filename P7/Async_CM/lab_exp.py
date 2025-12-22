import asyncio

class AsyncDatabase:
    def __init__(self, db_name):
        self.db_name = db_name

    async def __aenter__(self):
        print(f"Connecting to {self.db_name}...")
        await asyncio.sleep(1) 
        print(f"Connected to {self.db_name}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}...")
        await asyncio.sleep(0.5)
        print(f"Connection Closed.")

    async def query(self, sql):
        print(f"   Executing: {sql}")
        await asyncio.sleep(0.5)
        return "Result Data"

async def main():
    async with AsyncDatabase("Postgres_DB") as db:
        await db.query("SELECT * FROM users")

if __name__ == "__main__":
    asyncio.run(main())