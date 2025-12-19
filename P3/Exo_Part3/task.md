Task: Create a class `SafeWriter`.

- \_\_init__: Accepts a filename.

- \_\_enter__: Opens the file in "append" mode ("a"). Returns the file object.

- \_\_exit__: Closes the file object. Prints "File closed safely.".

Usage: Use a with statement to write the text "OOP is all you need\n" to a file named log.txt.

---