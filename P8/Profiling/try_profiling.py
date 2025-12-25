"""
Run the Profiler:
- In your terminal, run: python -m cProfile -s cumtime scripy.py
- Note: -s cumtime sorts the results by cumulative time (most useful).

Analyze the Output: Look at the top few rows.

The Question: Which internal function is the bottleneck?
- Is it clean_text?
- Is it db_lookup?
- Is it format_user?
 
"""

import time
import re

def clean_text(text):
    return re.sub(r"[^a-zA-Z]", "", text)

def db_lookup(user_id):
    time.sleep(0.001) 
    return f"User_{user_id}"

def format_user(user_id):
    name = db_lookup(user_id)
    clean = clean_text(name)
    return f"ID: {user_id} | Name: {clean}"

def main():
    print("Starting processing...")
    for i in range(1000):
        format_user(i)
    print("Done.")

if __name__ == "__main__":
    main()