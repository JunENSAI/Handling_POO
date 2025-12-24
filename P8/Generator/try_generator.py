"""
Task:
- Create a generator function id_stream():
    - It should use a while True: loop (normally dangerous, but safe with yield).

- In your main block:
    - Create the generator object: stream = id_stream().
    - Use a for loop to print the first 5 IDs only.
"""

def id_stream():
    id = 0
    while True:
        id+=1
        yield f"User_ID {id}"

def main():
    stream = id_stream()
    for i in range(5):
        print(next(stream))

if __name__=="__main__":
    main()