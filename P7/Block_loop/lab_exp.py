import asyncio
import time

# GOOD: Non-blocking
async def fry_eggs():
    print(" Starting Eggs...")
    await asyncio.sleep(2)
    print(" Eggs Ready!")

# BAD: Blocking
async def make_toast():
    print(" Starting Toast...")
    time.sleep(4) 
    print(" Toast Ready!")

async def make_coffee():
    print("Starting coffee...")
    await asyncio.sleep(1)
    print("coffee ready")

async def breakfast():
    await asyncio.gather(fry_eggs(), make_toast(), make_coffee())

if __name__ == "__main__":
    start = time.time()
    asyncio.run(breakfast())
    print(f"Total time: {time.time() - start:.2f} seconds")