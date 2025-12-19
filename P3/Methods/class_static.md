Inside a class, not every function needs self.

## 1. @classmethod (The Factory)

- **Arguments:** Receives cls (the class itself) instead of self.

- **Use Case:** Alternative constructors. "I want to create an object, but my data is in a weird format (like a string or dict)."

---

## 2. @staticmethod (The Utility)

- **Arguments:** Receives nothing special (no self, no cls).

- **Use Case:** Helper functions that belong logically to the class but don't touch its data.

---