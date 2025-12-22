"""
We are going to migrate the User.save() logic concept to Async.

Task:

Write a script that:

    - Connects to your db_poo database using asyncpg.

    - Inserts a New User named "async_user" with the role "bot".

        - Hint: await conn.execute("INSERT INTO users ...").

    - Fetches that specific user back using a SELECT statement.

    - Prints "Verified: Found async_user".
"""

import asyncio
import asyncpg

async def save():

    # etablish the connection
    conn = await asyncpg.connect(
        user="poo_user",
        password="poo_train36",
        database="db_poo",
        host="localhost"
    )

    try:
        print("Query to add new user")

        await conn.execute("INSERT INTO users (username, role) VALUES ('async_user', 'bot')")

        values = await conn.fetch("SELECT * FROM users")
        
        for row in values:
            print(f"User Found: {row['username']} (Role: {row['role']})")
    finally:
        await conn.close()
        print("Connection Closed.")

if __name__ == "__main__":
    asyncio.run(save())


