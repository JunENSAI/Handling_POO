import asyncio
import time

# --- (Sync) ---
def brew_coffee_sync():
    print("☕ Starting Coffee (Sync)...")
    time.sleep(2) 
    print("Coffee Ready (Sync)!")

# --- (Async) ---
async def brew_coffee_async():
    print("☕ Starting Coffee (Async)...")
    await asyncio.sleep(2) 
    print("Coffee Ready (Async)!")

async def main():
    print("--- STARTING ASYNC BATCH ---")
    await asyncio.gather(brew_coffee_async(), brew_coffee_async())

if __name__ == "__main__":
    # Sync take 4 seconds because task executed sequentially so 2 seconds for the first and 2 seconds for the second
    start = time.time()
    brew_coffee_sync()
    brew_coffee_sync()
    print(f"Sync took: {time.time() - start:.2f} seconds\n")

    # async take only 2 seconds because it does the task on parallelized way
    start = time.time()
    asyncio.run(main())
    print(f"Async took: {time.time() - start:.2f} seconds")