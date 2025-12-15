- Create a class called PostgresTable.

- The Constructor (__init__):

    - Accepts table_name (string) and columns (a list of strings).

    - Stores them as Instance Attributes.

    - Creates an empty list called rows (Instance Attribute).

- Class Attribute:

    - Add a variable database_type = "PostgreSQL" at the class level.

- Method insert(row_data):

    - Accepts a dictionary row_data.

    - Checks if the keys in row_data match the columns defined in __init__.

    - If they match, append the dict to self.rows.

    - If they don't match, print an error.

- Method select_all():

    - Returns the list of rows.