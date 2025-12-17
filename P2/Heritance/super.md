Inheritance allows a `class (Child)` to derive attributes and methods from another `class (Parent)`. This promotes code reuse and logical hierarchy.

## 1. The `super()` 

super() is a built-in function that returns a temporary object of the superclass (parent). It allows you to call methods of the parent that you might have overridden.

Why not just call `ParentClass.method(self)?`

=> Because if you change the name of the Parent class later, you have to find and replace it everywhere. `super()` handles this dynamic link automatically. It also handles complex "Multiple Inheritance" correctly via the MRO (**Method Resolution Order**).

---

## 2. Method Overriding

When a child class defines a method with the same name as a parent class, the child's method replaces the parent's.

- **Complete Override:** The child ignores the parent's logic entirely.

- **Extension (using super):** The child runs the parent's logic, then adds its own.

---