## 1. The Core Problem: Network Latency (RTT)

When your Python code talks to a Database, it isn't instantaneous. It has to travel over a network wire (even localhost has overhead). This travel time is called RTT (Round Trip Time).

### Scenario: You want to insert 1,000 users.

**The Naive Approach (The Loop):**

- **Python:** "Here is User 1" -> (Network) -> DB.

- **DB:** (Processing) -> "OK" -> (Network) -> Python.

- **Python:** "Here is User 2"...

*If the RTT is 1ms (which is fast), doing this 1,000 times takes 1 full second just in travel time, ignoring the actual work.*

---

## 2. The Solution: Batching (executemany)

Batching changes the architecture of the conversation. Instead of 1,000 small envelopes, we send one heavy box.

- **Python:** "Here is a list of 1,000 users." -> (Network) -> DB.

- **DB:** (Processing all 1,000) -> "OK" -> (Network) -> Python.

- **Result:** You pay the RTT penalty only once.

---

## 3. Why asyncpg wins here

While standard libraries like psycopg2 support batching, asyncpg is architected using the PostgreSQL Binary Protocol.

- **Text Protocol (psycopg2):** Converts 123 to string "123", sends it, DB converts back to int.

- **Binary Protocol (asyncpg):** Sends the raw bytes of the integer. No conversion overhead.

Combined with the non-blocking nature of Async IO (the CPU prepares the next batch while the previous one is transmitting), this results in massive throughput gains.

---

## 4. Key Takeaway

- Loops are the enemy of Database Performance.

- Never run an `INSERT` or `UPDATE` inside a for loop if you can avoid it.

- Always look for a "Bulk" or "Batch" method (like `executemany`).

---

## 5. Task

Write the Async script.

- Import `asyncio`, `asyncpg`, `time`.

- Generate a list of tuples for 1000 users: `data = [(f"async_{i}", "speeder") for i in range(1000)]`.

- **Connect to the DB.**

- Start the timer (`time.time()`).

- The Critical Step: Use await conn.executemany(...) to insert the whole list at once.

- Syntax: `await conn.executemany("INSERT INTO users (username, role) VALUES ($1, $2)", data)`

- **Note**: asyncpg uses `$1, $2 placeholders, NOT %s.`

- Stop the timer and print the result.

---