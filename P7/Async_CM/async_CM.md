## 1. Purpose of Async Context Managers

- You already know standard Context Managers (with open(...)) using `__enter__` and `__exit__`. But what if opening the resource requires awaiting?

- Connecting to a database over the network?

- Starting a secure SSL session?

- You cannot put await inside a standard `__enter__` method because it is synchronous. Python solved this by introducing Async Context Managers: async with.

---

## 2. Why it is Relevant

This is standard practice for modern IO libraries (aiohttp, asyncpg). It ensures that resources are initialized asynchronously and cleaned up automatically, even if errors occur.

Instead of `__enter__` and `__exit__`, we use:

    - async def __aenter__(self)**: Ran when entering the async with block.

    - async def __aexit__(self, exc_type, exc, tb): Ran when exiting.

---

## 3. How it Works Conceptually

**Start:** async with Database() as db:

    - __aenter__: Python pauses execution (await) while the connection is established.

**Body**: You run your queries.

    - __aexit__: Python pauses execution again (await) while the connection closes gracefully.

---

## 4. Key Takeaway

Use `async` with when the setup or teardown of a resource involves I/O (waiting).