Python has three levels of visibility.

## 1. Public (name)

Accessible from anywhere.

Example: `self.table_name`

---

## 2. Protected (`_name`) - The Convention

A single underscore prefix.

- **Meaning**: "This is internal. If you touch this from outside the class, and the code breaks, it's your fault."

- **Reality**: Python allows you to access it, but IDEs (like VS Code/PyCharm) will warn you.

---

3. Private (``__name``) - Name Mangling

Double underscore prefix.

- **Meaning**: "Do not touch."

- **Reality**: Python actively changes the name of variable in memory so you can't accidentally access it.

- **Mechanism**: self.__rows becomes _PostgresTable__rows in memory.

---