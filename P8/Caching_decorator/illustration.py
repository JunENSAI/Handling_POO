import time
from functools import lru_cache

# 1. No cache
def fib_slow(n):
    if n < 2:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

# 2. With cache
@lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    return fib_fast(n-1) + fib_fast(n-2)

def main():
    n = 35
    
    print(f"Calculating Fibonacci({n}) without cache...")
    start = time.time()
    print(f"Result: {fib_slow(n)}")
    print(f"Time: {time.time() - start:.4f} seconds")

    print("-" * 30)

    print(f"Calculating Fibonacci({n}) WITH cache...")
    start = time.time()
    print(f"Result: {fib_fast(n)}")
    print(f"Time: {time.time() - start:.4f} seconds")

if __name__ == "__main__":
    main()