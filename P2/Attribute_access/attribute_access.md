In many languages like **Java or C++**, encapsulation is enforced strictly. You hide variables and expose `getVariable()` and `setVariable()` methods.

We start with public attributes. If we need to add logic later (like validation), we don't break the code by changing to methods; we use Properties.

---

## 1. The Problem with Standard Getters/Setters

In **Java**, you might write:

```Java
// Java style (Verbose)
obj.setVoltage(120);
int v = obj.getVoltage();
```
In Python, this is considered "un-Pythonic" because it makes the code noisy. We prefer:

```Python
obj.voltage = 120
print(obj.voltage)
```

But what if voltage cannot be negative? If we just use `obj.voltage = -50`, the object is corrupted. This is where `@property` saves us.

---

## 2. The `property` Decorator

This decorator allows a method to be accessed as if it were an attribute. It gives you the clean syntax of obj.value but runs the code of def value(self): in the background.

Implementation Steps:

- **The Getter (@property)**: Defines how to read the value.

- **The Setter (@name.setter)**: Defines how to write the value (and validate it).

- **The Deleter (@name.deleter)**: Defines what happens if you run del obj.name.

---
