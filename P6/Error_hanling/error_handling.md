## 1. Purpose of Error Handling Architecture

Error Handling Architecture is the strategic design of how an application detects, reports, and recovers from unexpected states. 

Instead of letting the program crash (terminate) when something goes wrong, a robust architecture "catches" the error and decides what to do next (e.g., retry the connection, log the error, or show a polite message to the user).

---

## 2. Why Custom Exceptions are Relevant in OOP

In simple scripts, you might see except Exception:

- In Enterprise OOP, this is dangerous because it treats a "Database Offline" error the same as a "User Not Found" error.

- **Semantic Meaning:** by creating classes like PaymentFailedError or UserNotFoundError, the code becomes self-documenting. The error name tells you exactly what went wrong.

- **Granular Control** : You can catch specific errors and ignore others.

- **Catch:** NetworkError (Retry the request).

- **Don't Catch:** LogicError (Let it crash so developers see the bug).

---

## 3. How it Works Conceptually

The Hierarchy

Exceptions in Python are Classes. We use Inheritance to group them.

- MyAppError (Parent)

- DatabaseError (Child)

- ValidationError (Child)

- Bubbling Up

When an error occurs deep in a function, it "bubbles up" the call stack until it finds a try/except block that can handle it. If it reaches the top without being caught, the program crashes.

---

## 4. When to Use Custom Exceptions

- **Library Design:** When you are building code for others (or yourself) to use. You want to tell them exactly why your library failed.

- **Business Logic:** When a state is invalid but not a "bug" (e.g., "Insufficient Funds" is an exception, not a code crash).

- **layer Separation:** The Database layer should raise DatabaseError, which the API layer catches and converts into an HTTP 500 response.

---

## 5. Key Takeaway

- Error Architecture is about Resilience.

- It transforms "crashes" into "handled events."

- By using a Class Hierarchy for errors, you gain the power to treat different failures differently.

---