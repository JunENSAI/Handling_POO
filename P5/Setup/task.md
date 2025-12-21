We need to install the driver and establish a connection. Since you have Postgres installed, we will use the library psycopg2 (or psycopg2-binary).

## Task 1

Write a script that:

- Imports psycopg2.

- Defines a Database class (Singleton).

- In __init__, it connects to your local Postgres database.

- **Tip:** You need `self.connection = psycopg2.connect(...)`.

- Provides a method `get_connection(self)` that returns the connection object.

---

## Task 2

- Create the Model class.

- Class Attribute: Add table_name = "" (empty by default).

- __init__:

    - Accept **kwargs (keyword arguments).

    - Loop through the kwargs items.

    - For every key/value, set it as an attribute on the object using setattr(self, key, value).

    - Why? This turns User(name="Alice") into self.name = "Alice" automatically.

---