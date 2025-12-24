## 1. What is Big O?

`Big O` is how we measure how execution time grows as the input size (N) grows. We don't measure seconds (because different computers are faster/slower). We measure Operations.

---

## 2. The Big 3 Categories

### O(1) - Constant Time

No matter how much data you have, it takes the same amount of time.

- **Example:** Accessing a list by index users[0].

- **Analogy:** Shaking hands with the first person in a line. It takes 5 seconds whether the line has 1 person or 1,000 people.

### O(N) - Linear Time (Okay)

If you double the data, you double the time.

- **Example:** Finding a user in a list for u in users: if u == "Alice".

- **Analogy:** Shaking hands with everyone in the line. 10 people = 50 seconds. 1,000 people = 5,000 seconds.

### O(N²) - Quadratic Time

If you double the data, the time quadruples.

- **Example:** Nested Loops. Comparing every user to every other user.

- **Analogy:** Everyone in the line has to shake hands with everyone else in the line.

- `1,000 people = 1,000,000 handshakes. (The server crashes).`

---