"""
Task :

- Write an async function compute_square(n):

    - Print "Computing..."
    - await asyncio.sleep(1)
    - Return n * n.

- Write a main function:

    - Use await asyncio.gather(...) to compute squares for 2, 3, and 4.
    - Capture the result: results = await asyncio.gather(...)
    - Print the results.
"""

import asyncio
import time

async def compute_square(n):
    print("Computing...")
    await asyncio.sleep(1)
    return n*n

async def main():
    print("Start compute square")
    results = await asyncio.gather(compute_square(2), compute_square(3), compute_square(4))
    print("Results \n", results)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"Total time: {time.time() - start:.2f} seconds")