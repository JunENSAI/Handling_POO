import time
import random

def has_duplicates_quadratic(ids_list):
    """ This function has a complexity equal to O(N^2) because the clause if here
        scan all the list so the number of operation during the search is O(N)
    """
    unique_ids = []
    for id in ids_list: 
        if id in unique_ids: 
            return True
        unique_ids.append(id)
    return False


def has_duplicates_linear(ids_list):
    unique_ids = set()
    for id in ids_list: 
        if id in unique_ids: 
            return True
        unique_ids.add(id)
    return False

def comparsion(ids_list):
    
    # Linear
    start = time.time()
    has_duplicates_linear(ids_list)
    print(f"O(N)  Time: {time.time() - start:.5f} sec")

    # Quadratic
    start = time.time()
    has_duplicates_quadratic(ids_list)
    print(f"O(N²) Time: {time.time() - start:.5f} sec")


l = liste_nombres = [random.randint(0, 1000000) for _ in range(100000)]

comparsion([random.randint(0, 10000) for _ in range(10000)])

#Results : O(N)  Time: 0.00002 sec | O(N²) Time: 0.00005 sec
