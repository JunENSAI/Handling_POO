Objects are useful because they maintain State. A method's job is often to modify that state safely.

## 1. Meaningful Methods

A method should usually do one of two things:

- **Command:** Change the state of the object (return `None`).

- **Query:** Return a value based on the state (don't change anything). Trying to do both is often bad design.

---