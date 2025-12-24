import sys

# 1. Standard List
def get_list(n):
    return [i for i in range(n)]

# 2. Generator
def get_generator(n):
    for i in range(n):
        yield i

def compare_memory():
    n = 1_000_000
    
    # LIST
    my_list = get_list(n)
    print(f"List Size in RAM: {sys.getsizeof(my_list)} bytes") # 8448728 bytes

    # GENERATOR
    my_gen = get_generator(n)
    print(f"Generator Size in RAM: {sys.getsizeof(my_gen)} bytes") # 200 bytes

compare_memory()