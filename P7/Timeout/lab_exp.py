import asyncio

async def slow_api():
    print(" API: starting request...")
    await asyncio.sleep(5)
    return "Data Received!"

async def main():
    try:
        print("System: Waiting for data (max 2s)...")
        result = await asyncio.wait_for(slow_api(), timeout=2.0)
        print(result)
        
    except asyncio.TimeoutError:
        print("Error: The API took too long! Request cancelled.")

if __name__ == "__main__":
    asyncio.run(main())