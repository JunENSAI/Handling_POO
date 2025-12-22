"""
Task:

    - Write an Async function called download_file.

    - It should print "Downloading..."

    - It should wait for 1 second.

    - It should print "Download Complete."

    - Write a main block that runs download_file 3 times concurrently using asyncio.gather.

    - Run it.
"""

import asyncio
import time

async def download_file():
    print("Downloading...")
    await asyncio.sleep(1)
    print("Download Complete")

async def main():
    await asyncio.gather(download_file(), download_file(), download_file())

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"Async took: {time.time() - start:.2f} seconds")