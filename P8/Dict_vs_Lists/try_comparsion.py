"""
Task : 

- Create a class SecuritySystem.
    - __init__: Accepts a list of banned_ips. Optimize the search of banned_ips...
    - is_banned(ip): Checks if the IP is banned or not and returns True/False.

- main:
    - Generate a "fake" blacklist of 1 million IPs.
    - Initialize your SecuritySystem with this list.
    - Measure how long it takes to check a specific IP.
"""

from typing import List
import time

class SecuritySystem:

    def __init__(self, banned_ips: List[str]):
        self.banned_set = set(banned_ips)
    
    def is_banned(self,ip):
        if ip in self.banned_set:
            return True
        return False
    
def main():
    ip_list = [f"198.01.01.'{i}" for i in range(1000000)]

    ss = SecuritySystem(ip_list)

    start = time.time()

    ss.is_banned("198.01.01.999999")

    print(f"It took {time.time() - start:.6f} seconds ")

if __name__ == '__main__':
    main()