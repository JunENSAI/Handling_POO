class PostgresTable:

    database_type = "PostgreSQL"

    def __init__(self, table_name:str, columns:list[str]):
        self.table_name = table_name
        self.columns = columns
        self.rows = []
    
    def insert_row(self, row:dict):
        if set(row.keys()) == set(self.columns):
            self.rows.append(row)
        else:
            raise ValueError("Row keys do not match table columns")
    
    def select_all(self):
        return self.rows
    
