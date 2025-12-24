## 1. The Core Problem: Memory Constraints

In standard Python (and most languages), functions are "Eager." When you call `get_users()`, it calculates every single user and stores them in a List in Random Access Memory (RAM) before giving you the result.

- **Scenario:** You query 1,000,000 rows from a database.

- **The List Approach:** Python tries to allocate 500MB of RAM to hold the list. If your server only has 256MB, the program crashes with `MemoryError`.

---

## 2. The Solution: Lazy Evaluation (Generators)

A `Generator` is a function that remembers where it left off. Instead of calculating everything at once, it calculates one item at a time, hands it to you, and then pauses execution.

- **The List Approach**: "Here are 1 million apples. Carry them all at once." (Heavy).

- **The Generator Approach**: "Here is one apple. Eat it. Come back when you want another." (Light).

---

## 3. How it Works Conceptually

The `yield` Keyword

- **return:** Terminates the function and destroys local variables.

- **yield:** Pauses the function, saves its state (variables, line number), and ejects the value to the caller. When called again (via next()), it resumes exactly where it left off.

### The Pipeline Architecture

Generators allow you to build "Processing Pipelines."

- Generator A reads lines from a 100GB file (1 by 1).

- Generator B filters them (1 by 1).

- Generator C writes them to a new file (1 by 1).

- **Result:** You process 100GB of data using only 1KB of RAM.

---

## 4. Key Takeaway

- Use `Lists ([])` when you need random access (e.g., "Give me the 50th item") or the data is small.

- Use `Generators (yield)` when the data is massive or infinite (e.g., a stream of sensor data).

---