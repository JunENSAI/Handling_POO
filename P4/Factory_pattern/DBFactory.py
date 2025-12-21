class PostgresTable:

    database_type = "PostgreSQL"

    def __init__(self, table_name:str, columns:list[str]):
        self.table_name = table_name
        self.columns = columns
        self.rows = []

    def __repr__(self):
        return f"PostgresTable(table_name = '{self.table_name}', columns = '{self.columns}')"
    
    def insert_row(self, row:dict):
        if set(row.keys()) == set(self.columns):
            self._rows.append(row)
        else:
            raise ValueError("Row keys do not match table columns")
    
    def select_all(self):
        return self.rows
    
    def access_connect(self):
        print(f"Postgresql must be connected on {self.connect_string.connect()}")

class CSVTable:

    def __init__(self, table_name:str):
        self.table_name = table_name


class DBFactory:
    
    @staticmethod
    def get_table(db_type, table_name):
        if db_type == "postgres":
            return PostgresTable(table_name, [])
        elif db_type == "csv":
            return CSVTable(table_name)
        else:
            raise ValueError("Unknown Database Type")

tbl = DBFactory.get_table("postgres", "users")

print([tbl])

