## Task 1: Secure the Parent Modify your PostgresTable class:

- Change `self.rows` to be Protected (`self._rows`).

- Change `self.columns` to be Protected (`self._columns`).

- Add a `@property` for columns. It should return the list of columns.

- **Important: Do NOT add a setter for columns. (Once a table is created, you shouldn't be able to change its column structure in this simple model). This makes it "Read-Only"**.

---

## Task 2: Create a Child Class Create a new class LogTable that inherits from PostgresTable.

- It should automatically set the table_name to "system_logs" inside its own `__init__`.

- It should override `insert_row`:

    - Before inserting, it should automatically add a key "created_at" with the value "NOW()" to the row data (simulating a timestamp).

    - Then, it should use `super().insert_row()` to actually save the data.

---