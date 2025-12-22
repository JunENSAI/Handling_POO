import asyncpg
import time
import asyncio
from typing import List, Tuple

class AsyncImporter:

    def __init__(self, dsn:str):
        self.dsn = dsn
        self.conn = None

    async def __aenter__(self):
        self.conn = await asyncpg.connect(self.dsn)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()
    
    async def import_user(self,users_list:List[Tuple[str, str]]):
        await self.conn.executemany(
            "INSERT INTO users (username, role) VALUES ($1, $2)", 
            users_list
        )


async def main():

    users_list = [(f"user_{i}", "bulk") for i in range(10000)]

    dsn = "postgresql://poo_user:poo_train36@localhost/db_poo"

    start = time.time()
    
    async with AsyncImporter(dsn) as importer:
        await importer.import_user(users_list)

    end = time.time()

    print(f"It tooks: {end - start:.4f} seconds")


if __name__ == "__main__":
    asyncio.run(main())