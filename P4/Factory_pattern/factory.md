## 1. Purpose of the Factory

The Factory pattern is a creational pattern that defines an interface for creating an object, but lets subclasses or helper methods decide which class to instantiate. It is used to separate the creation logic from the business logic.

---

## 2. Why Factory is Relevant in OOP
This is the ultimate implementation of the Dependency Inversion Principle:

- **Loose Coupling**

The main application code (client) does not need to know the specific class name (e.g., PostgresConnection) it is using. It only needs to know the interface (e.g., Connection).

- **Open/Closed Principle (OCP)**

You can introduce new types of objects (e.g., MongoConnection) into the program without breaking or changing the existing client code. You only update the Factory.

---

## 3. How it Works Conceptually

The Client's Request: The client asks the Factory: "I need a Database."

- **The Logic:** The Factory checks configuration or parameters (e.g., "Config says we are in 'Production'").

- **The Decision:** The Factory silently selects the correct class (PostgresTable) without the client knowing.

- **The Delivery:** It returns the object.

---

## 4. When to Use Factory

You don't know beforehand the exact types and dependencies of the objects your code should work with.

You want to provide a library or framework to users who will extend your components.

You want to centralize complex object creation logic (e.g., objects that require 5 arguments to set up).

---

## 5. Key Takeaway

- Factory is about **Abstraction**.

- It allows your code to work with "Concepts" (like Any Database) rather than "Concretions" (like PostgreSQL v14).

---