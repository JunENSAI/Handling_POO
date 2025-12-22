## 1. The Distinction

- **Blocking:** Control is held by a single line of code. The entire application stops until that line finishes.

- **Non-Blocking:** The function submits a request and immediately returns control to the loop, promising to handle the result later.

---

## 2. The "Poison" of Blocking Code

In an async application, Time is a shared resource. If you use a blocking function (like time.sleep or a heavy math calculation) inside an async function, you "starve" the Event Loop.

- **User A** asks for a calculation.

- **User B** tries to login.

Because User A blocked the loop, User B's login request is ignored until User A finishes.

---

## 3. How to Avoid It

- Never use `time.sleep()`; use `await asyncio.sleep()`.

- Never use standard requests.get(); use `aiohttp or httpx`.

- Never use standard `psycopg2 (for DB)`; use `asyncpg`.

---

## 4. Key Takeaway

- "Don't Block the Loop."

- One blocking function ruins the performance of the entire asynchronous system.

---