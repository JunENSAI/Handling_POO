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

## Task 3

- Add the save() method to your Model class.

- **Requirements:**

    - Get the connection from your Database() Singleton.

    - Create a cursor: cursor = connection.cursor().

    -  the SQL:

    - Join the keys with commas to make the column string.

    - Create the placeholder string (e.g., %s, %s, %s).

    - Format string: f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"

    - Execute: cursor.execute(sql, values).

    - Commit: connection.commit() (Crucial! Without this, data isn't saved).

    - Close: Close the cursor.