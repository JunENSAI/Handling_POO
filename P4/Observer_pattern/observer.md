## 1. Purpose of the Observer

The Observer pattern is a behavioral design pattern that defines a subscription mechanism to notify multiple objects about any events that happen to the object they are observing. It is the backbone of Event-Driven Architecture.

---

## 2. Why Observer is Relevant in OOP
This pattern solves the problem of tightly coupled components.

- **Decoupling**

The object changing state (the Subject) does not need to know who is listening or what they will do. It just broadcasts a signal.

- **Dynamic Relationships**

You can add or remove listeners (Observers) at runtime without stopping the application.

---

## 3. How it Works Conceptually

- **Subscription:** Objects (Observers) register themselves with the Subject ("Tell me when you update").

- **State Change:** The Subject performs an action (e.g., insert_row).

- **Notification:** The Subject iterates through its list of subscribers and calls a specific method on each one (e.g., .update()).

---

## 4. When to Use Observer

- When changes to one object require changing others, and you don't know how many objects need to be changed.

- When an object should be able to notify other objects without making assumptions about who these objects are.

- In UI elements (e.g., "Button Clicked" -> Notify "Animation", "Sound", and "Database").

---

## 5. Key Takeaway

- Observer is about **Communication**. 

- It allows a 1-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

---