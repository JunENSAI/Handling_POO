To understand Async, you must understand the Event Loop.

**Imagine a Waiter (Python) in a restaurant (CPU).**

## Scenario A: Synchronous (Blocking)

- Waiter takes Order 1.

- Waiter walks to the kitchen.

- Waiter stands there and stares at the chef for 10 minutes until the food is ready.

- Waiter serves Order 1.

- Only then does the Waiter take Order 2.

- Result: The restaurant is slow.

## Scenario B: Asynchronous (Non-Blocking)

- Waiter takes Order 1.

- Waiter passes the ticket to the kitchen.

- Waiter immediately goes back to take Order 2.

- Kitchen rings a bell ("Callback").

- Waiter grabs the food and serves Order 1.

- Result: One waiter handles 50 tables efficiently.

---

*In Python, we use two keywords to control this:*

- `async def`: Defines a function that can be paused (a "Coroutine").

- `await`: Tells Python "Pause here, go do other work, and come back when this finishes."