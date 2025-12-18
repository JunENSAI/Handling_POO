Polymorphism comes from Greek: `"Poly" (many) + "Morph" (forms)`. It allows different objects to respond to the same method call in their own unique way.

In strictly typed languages (Java, C++), this is complex. In Python, it is effortless because of Duck Typing.

## 1. What is Duck Typing?

**If it walks like a duck and quacks like a duck, then it must be a duck.**

Python does not check the Type of the object; it checks the Capabilities (methods/attributes) of the object.

If you have a function `make_sound(animal)`, Python doesn't care if animal is a Dog, a Cat, or a Car. It only cares: "Does this object have a .speak() method?" If yes, it runs. If no, it crashes.

---