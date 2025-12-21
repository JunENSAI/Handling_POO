## 1. The "Scripting" Trap
Most beginners write code like this:

- Write a function.

- Add print(my_func()) at the bottom.

- Run it.

- Delete the print statement.

- The Problem: You just deleted your proof! If you change the function 6 months later, you have to manually re-test everything.

---

## 2. The TDD Solution

Test Driven Development suggests a different workflow:

- **Red:** Write a test that fails (because the feature doesn't exist yet).

- **Green:** Write just enough code to pass the test.

- **Refactor:** Clean up the code while keeping the test green.

---

## 3. Why pytest?

Python has a built-in library called unittest (based on Java's JUnit). It requires writing classes for every test. Pytest is the modern standard because:

- It uses simple assert statements.

- It has powerful plugins (coverage, async, django support).

- It supports Fixtures (see Day 2).
---