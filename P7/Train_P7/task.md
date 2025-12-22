## The Scenario: 

- You have a CSV file (simulated) with 100,000 rows.

- You need to import it into Postgres without crashing your computer or the database.

- **The Architecture:** We will use a class AsyncImporter that uses an Async Context Manager (`__aenter__`) to connect, and a method import_data that takes a list and batches it.

---

## Task:

- Create a class AsyncImporter.

    `__init__`: Accepts dsn (the connection string: `"postgresql://user:pass@localhost/db"`).

    `__aenter__`: Connects to the DB.

    `__aexit__`: Closes the connection.

- import_users(users_list):

    - Uses `await self.conn.executemany(...) `to insert the users.

- main:

    - Generates a list of 10,000 users: [(f"user_{i}", "bulk") for i in range(10000)].

    - Uses async with AsyncImporter(...) as importer:

    - Calls the import function.

    - Measures and prints the time.
---