## 1. Purpose of the Singleton

The Singleton pattern is a creational design pattern that ensures a class has only one instance globally and provides a global point of access to it. It is primarily used to manage shared resources, such as:

- Database connections

- Configuration settings

- Logging handles

- Caching mechanisms

---

## 2. Why Singleton is Relevant in OOP
From an architecture standpoint, Singleton addresses specific constraint requirements:

- Resource Control

It prevents the system from opening too many connections (e.g., to a database) which could crash the external service.

- Global State Consistency

It ensures that if one part of the app changes a setting (like Debug Mode = True), that change is immediately reflected across the entire application, because everyone is looking at the exact same object.

---

## 3. How it Works Conceptually

A Singleton operates by hijacking the object creation process:

- Interception: It overrides the default constructor mechanism (__new__ in Python).

- Check: It checks if an instance already exists in a private class-level variable.

- Return:

    - If No: It creates the instance, saves it, and returns it.

    - If Yes: It returns the existing saved instance without creating a new one.

---

## 4. Singleton vs. Static Class
While they look similar, a Singleton is better in OOP because:

- It can implement interfaces (Polymorphism).

- It can be passed as a parameter to other methods.

- It can be lazy-loaded (created only when first needed).

---

## 5. When to Use Singleton

Exactly one instance is required to coordinate actions across the system.

Strict control over global variables is needed.

## 6. Key Takeaway

- Singleton is about Controlled Access. 

- It trades the flexibility of instantiation for the safety of a guaranteed unique state.

---