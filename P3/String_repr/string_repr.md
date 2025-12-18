## String Representation (__str__ vs __repr__)

By default, Python objects are ugly. When you print a custom object, you get: `<__main__.PostgresTable object at 0x7f9b1c2>` This tells you where it is in memory, but not what it is.

We fix this using two specific magic methods.

### 1. __str__(self): The "End-User" Display

This method is called when you use print(obj) or str(obj).

- **Target Audience:** The customer, the end-user, or the logs.

- **Goal:** Readability. It should look nice.

- **Example:** "Order #455 - $99.00"

---

### 2. __repr__(self): The "Developer" Display

This method is called when you inspect an object in the shell, use the debugger, or call repr(obj).

- **Target Audience:** You (the programmer).

- **Goal:** Ambiguity reduction.

- **Golden Rule:** If possible, the string returned by `__repr__` should be valid Python code that recreates the object.

- **Good:** "User(id=1, name='Bob')"

- **Bad:** "User Bob"

---