Polymorphism is great, but it's dangerous. What if you create a new class **WavFile** but you forget to write the `.play()` method? Your program will crash at runtime.

Abstraction fixes this by enforcing a Contract.

## 1. Abstract Base Classes (ABC)

We use Python's built-in abc module.

- **Abstract Class:** A class that cannot be instantiated (you can't make an object from it). It exists only to be a parent.

- **Abstract Method:** A method with no body (just pass). It forces the child class to write the implementation.

---