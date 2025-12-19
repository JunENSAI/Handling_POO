You know how `for x in list`: works. But how does Python know how to loop over the list? It asks for an Iterator.

To make your object loopable, you have two options:

- **The Easy Way:** Delegate to an internal list (most common).

- **The Hard Way **: Implement `__iter__` AND `__next__`.

---