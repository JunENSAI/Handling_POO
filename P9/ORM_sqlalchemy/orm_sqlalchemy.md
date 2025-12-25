## 1. The Problem: Writing SQL Strings

In P7, you wrote raw SQL: `INSERT INTO users VALUES ....`

- **Fragile:** If you rename a column in the DB, your Python strings break.

- **Insecure:** Easy to make mistakes (SQL Injection) if not careful.

- **Hard to Read:** Mixing Python and SQL logic is messy.

---

## 2. The Solution: ORM (Object Relational Mapper)

An ORM allows you to interact with your database using pure Python Classes.

- `Table = Python Class`

- `Row = Instance of that Class`

- `Column = Class Attribute`

You don't write INSERT. You just create a Python object and say `.add().`

---

## 3. The Tool: SQLAlchemy

This is the industry standard ORM for Python.

### The 3 Core Components

- **Engine:** The actual connection to the database (the "Driver").

- **Session:** The "staging area" where you create/modify objects before saving them.

- **Base:** The parent class that all your database models must inherit from.

---