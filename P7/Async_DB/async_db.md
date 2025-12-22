## 1. The Bottleneck of psycopg2

In P1, you used `psycopg2`. This is a robust driver, but it is Blocking. If you use `psycopg2` inside an async def function, the entire Event Loop stops while waiting for Postgres. This defeats the purpose of using async!

---

## 2. Enter asyncpg

`asyncpg` is a database interface library designed specifically for PostgreSQL and `Python/asyncio`.

- It is Non-Blocking (uses await).

- It is Incredibly Fast (often 3x faster than psycopg2).

- It handles connections differently (it doesn't typically use "cursors" in the same way).

---

## 3. Key Differences

| Feature  | psycopg2 (Sync)            | asyncpg (Async)                                      |
|----------|----------------------------|------------------------------------------------------|
| Connect  | `conn = connect(...)`       | `conn = await connect(...)`                          |
| Query    | `cursor.execute(sql)`       | `await conn.fetch(sql)`                              |
| Commit   | `conn.commit()`             | Automatic (simple queries) or explicit transactions |
| Context  | `with conn:`                | `async with conn.transaction():`                     |

---
