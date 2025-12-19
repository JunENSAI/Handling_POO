You have seen this pattern before:

```Python
with open("file.txt", "w") as f:
    f.write("Hello")
```

- **Why do we use it?**

=> It guarantees safety. Even if the code crashes inside the block, the file will close.

- How do we build our own? Need to implement two methods:

- \_\_enter__(self): Runs when you say with .... Returns the object to use.

- \_\_exit__(self, exc_type, exc_val, exc_tb): Runs when the block ends (or crashes). This is where you close DB connections.