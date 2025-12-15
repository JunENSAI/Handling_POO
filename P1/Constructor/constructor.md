You must distinguish between **Instance Attributes** and **Class Attributes**.

## 1. `__init__` (The Constructor)

This is not technically the first thing called (that's `__new__`), but it is the initializer. It sets up the initial state.

---

## 2. The Trap: Class vs. Instance

- **Instance Attribute** (`self.x`): Unique to that specific object. Stored in the object's `__dict__`.

- **Class Attribute (x defined outside methods)**: Shared by ALL instances. If you change a mutable class attribute (like a list), it changes for everyone.

---