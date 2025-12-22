"""
Task: 

- Create a class AsyncTimer that measures how long a block of code takes to run.

    - __aenter__:

        - Record the start_time (use time.time()).
        - Print "Timer started...".
        - Return the object instance (self).

    - __aexit__:
        - Calculate elapsed = time.time() - self.start_time.
        - Print "Timer stopped. Elapsed: X seconds".

- Usage (Main):
    - Use async with AsyncTimer():.
    - Inside the block, use await asyncio.sleep(1.5).
"""

import asyncio
import time

class AsyncTimer:

    async def __aenter__(self):
        self.start_time = time.time()
        print(f"Timer started...")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        print(f"Timer stopped. Elapsed: {elapsed} seconds")
        
async def main():
    async with AsyncTimer():
        await asyncio.sleep(1.5)

if __name__ == "__main__":
    asyncio.run(main())