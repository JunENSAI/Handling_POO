import time

# O(N): Simple Loop
def linear_search(n):
    data = range(n)
    count = 0
    for i in data:
        count += 1
    return count

# O(N^2): Nested Loop
def quadratic_search(n):
    data = range(n)
    count = 0
    for i in data:
        for j in data:
            count += 1
    return count

def comparsion(n):
    print(f"--- Processing N={n} ---")
    
    # Linear
    start = time.time()
    linear_search(n)
    print(f"O(N)  Time: {time.time() - start:.5f} sec")

    # Quadratic
    start = time.time()
    quadratic_search(n)
    print(f"O(N²) Time: {time.time() - start:.5f} sec")

comparsion(1000)
comparsion(5000) 
