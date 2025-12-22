"""
Results : 

    - Sync took: 0.1401 seconds

    - ASync took: 0.0090 seconds

"""

import psycopg2
import time
import asyncio
import asyncpg

def run_sync():
    conn = psycopg2.connect(
        user="poo_user",
        password="poo_train36",
        database="db_poo",
        host="localhost")
    
    cursor = conn.cursor()
    
    data = [(f"user_{i}", "grunt") for i in range(1000)]
    
    start = time.time()
    for u, r in data:
        cursor.execute("INSERT INTO users (username, role) VALUES (%s, %s)", (u, r))
    conn.commit()
    
    end = time.time()
    print(f"Sync took: {end - start:.4f} seconds")
    conn.close()

async def run_async():

    conn = await asyncpg.connect(
        user="poo_user",
        password="poo_train36",
        database="db_poo",
        host="localhost"
    )
    data = [(f"async_{i}", "speeder") for i in range(1000)]

    start = time.time()

    await conn.executemany("INSERT INTO users (username, role) VALUES ($1, $2)", data)

    end = time.time()

    print(f"ASync took: {end - start:.4f} seconds")
    await conn.close()

if __name__ == "__main__":
    run_sync()
    print("-" * 30)
    asyncio.run(run_async())