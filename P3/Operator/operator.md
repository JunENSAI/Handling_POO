Python allows you to change how standard math operators **(+, -, *, ==, <, >)** behave when applied to your custom objects. This is called Operator Overloading.

## 1. Equality: `__eq__(self, other)`

By default, `==` in Python checks if two variables point to the same location in memory (Identity). In data applications, we usually want to check if they have the same data (Equality).

**Logic:**

- Check if other is actually the same Class.

- Check if the critical attributes match.

---

## 2. Addition: `__add__(self, other)`

You can define what happens when you do `obj1 + obj2`.

**Example:** Adding two ShoppingCart objects together could merge their item lists.

---