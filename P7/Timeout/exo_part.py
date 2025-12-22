"""
Task :

- Create an async function download_file(file_name, duration).
    - It should print(f"Starting {file_name}").
    - It should await asyncio.sleep(duration).
    - It should return f"{file_name} downloaded".

- Create a main function.
    - It should try to download "File_A" which takes 1 second (Should succeed).
    - It should try to download "File_B" which takes 4 seconds (Should fail).
    - Crucial: Wrap the specific call for "File_B" in asyncio.wait_for with a timeout of 3 seconds.
- Use a try/except block to catch the TimeoutError for File B and print "File B timed out".
"""

import asyncio

async def download_file(file_name, duration):
    print(f"Starting {file_name}")
    await asyncio.sleep(duration)
    return f"{file_name} downloaded"

async def main():

    result_A = await asyncio.gather(download_file("File A", 1))
    print(result_A)
    try:
        print("System: Waiting for data (max 3s)...")
        
        result_B = await asyncio.wait_for(download_file("File B", 4), timeout=3.0)
        print(result_B)
        
    except asyncio.TimeoutError:
        print("Error: The download for file B take too long ")


if __name__ == "__main__":
    asyncio.run(main())