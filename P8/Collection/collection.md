## 1. The Core Problem: Lists are not Queues

In Python, a standard list is implemented as a dynamic array.

- **Append:** `list.append(x)` is O(1) (Fast).

- **Pop First:** `list.pop(0)` is O(N) (Slow).

Why? If you remove the first item, Python has to physically shift every other item one step to the left in memory.

If you are building a Queue (First-In-First-Out) using a list, your performance will degrade linearly.

---

## 2. The Solution: deque (Double-Ended Queue)

The collections module provides deque (pronounced "deck"). It is a Doubly Linked List.

- **Append:** O(1)

- **Pop Left:** O(1) (Instant, no shifting required).

---

## 3. Other Tools

- `Counter:` A dictionary subclass for counting hashable objects (e.g., counting word frequency).

- `namedtuple:` Factory function for creating tuple subclasses with named fields.

---