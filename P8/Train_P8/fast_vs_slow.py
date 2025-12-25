""" Currently, the script (find_valid_orders_slow()) takes ~17 seconds to process just 50,000 items. Your boss wants it done in < 0.1 seconds. """

import time
import random

valid_ids_list = [random.randint(0, 200000) for _ in range(50000)]

transactions = [{"id": random.randint(0, 200000), "amount": i} for i in range(50000)]

def find_valid_orders_slow():
    valid_orders = []
    print("Starting Processing")
    start = time.time()
    
    for trans in transactions:
        if trans["id"] in valid_ids_list:
            valid_orders.append(trans)
            
    print(f"Time: {time.time() - start:.4f} seconds")
    return valid_orders


def find_valid_orders_fast():
    valid_ids_set = set(valid_ids_list)

    print("Starting processing")
    start = time.time()
    try:
        for trans in transactions:
            if trans["id"] in valid_ids_set:
                yield trans
    finally:
        print(f"Time: {time.time() - start:.4f} seconds")



if __name__ == "__main__":
    find_valid_orders_slow()
    for _ in find_valid_orders_fast():
        pass
