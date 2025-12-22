import asyncio
import asyncpg

async def run_db_test():
    print("Connecting to Postgres (Async)...")
    
    # 1. Establish Connection
    conn = await asyncpg.connect(
        user="poo_user",
        password="poo_train36",
        database="db_poo",
        host="localhost"
    )

    try:
        # 2. Run a Query
        print("Executing Query...")
        values = await conn.fetch("SELECT * FROM users")
        
        # 3. Process Results
        for row in values:
            print(f"User Found: {row['username']} (Role: {row['role']})")
            
    finally:
        # 4. Close Connection
        await conn.close()
        print("Connection Closed.")

if __name__ == "__main__":
    asyncio.run(run_db_test())