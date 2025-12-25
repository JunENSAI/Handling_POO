import time
import random

def run_experiment():
    N = 10_000_000
    print(f"Generating {N} items...")
    
    # List:
    large_list = list(range(N))
    
    # Set
    large_set = set(range(N))

    target = N - 1 

    print("---  ---")

    # TEST 1: List Search
    start = time.time()
    found = target in large_list
    duration = time.time() - start
    print(f"List Search: {duration:.6f} seconds")

    # TEST 2: Set/Dict Search
    start = time.time()
    found = target in large_set
    duration = time.time() - start
    print(f"Set Search:  {duration:.6f} seconds")

if __name__ == "__main__":
    run_experiment()