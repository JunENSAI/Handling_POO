"""
Task:

- Create a function get_user_profile(user_id).
    - Add the decorator @lru_cache(maxsize=None).

- In main():
    - Call get_user_profile(1)
    - Call get_user_profile(1)
    - Call get_user_profile(2)

Watch the results !!
"""

import time
from functools import lru_cache

@lru_cache(maxsize=None)
def get_user_profile(user_id):
    print (f"Fetching data for {user_id} from DB...")
    time.sleep(2)
    return f"Profile for {user_id}"

def main():
    start_1 = time.time()
    get_user_profile(1)
    print(f"Time: {time.time() - start_1:.4f} seconds")

    start_2 = time.time()
    get_user_profile(1)
    print(f"Time: {time.time() - start_2:.4f} seconds")

    start_3 = time.time()
    get_user_profile(2)
    print(f"Time: {time.time() - start_3:.4f} seconds")

if __name__=='__main__':
    main()

