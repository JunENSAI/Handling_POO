## 1. The Core Problem: Redundant Calculation

In complex systems, we often call functions with the exact same arguments multiple times.

- **Scenario:** A function get_user_balance(user_id) involves a heavy database query.

- **The Waste:** If you call get_user_balance(5) ten times in one second, you hit the database ten times for the exact same result.

---

## 2. The Solution: Caching

Caching is the technique of storing the result of a function call. If the function is called again with the same arguments, you return the stored result instantly, skipping the calculation.

---

## 3. How it Works Conceptually (The Decorator)

A Decorator (`@wrapper`) is a function that wraps another function to modify its behavior. `Python's built-in functools.lru_cache` (Least Recently Used Cache) automatically handles this.

- Call 1: `calc(5) -> Computer runs logic -> Returns 10.` (Cache: {5: 10})

- Call 2: `calc(5) -> Computer checks Cache -> Finds 5 -> Returns 10.` (Instant).

---

## 4. Key Takeaway

- **Decorators** allow you to optimize code without changing the code itself.

- **Caching** is the easiest way to turn an O(2^N) algorithm into O(N).

---