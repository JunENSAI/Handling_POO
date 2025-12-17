class PostgresTable:

    database_type = "PostgreSQL"

    def __init__(self, table_name:str, columns:list[str]):
        self.table_name = table_name
        self._columns = columns
        self._rows = []
    
    @property
    def columns(self):
        return self._columns
    
    def insert_row(self, row:dict):
        if set(row.keys()) == set(self.columns):
            self._rows.append(row)
        else:
            raise ValueError("Row keys do not match table columns")
    
    def select_all(self):
        return self._rows

class LogTable(PostgresTable):
    def __init__(self):
        super().__init__("system_logs", ["message", "level", "created_at"])
    
    def insert_row(self, row:dict):

        row["created_at"] = "NOW"
        super().insert_row(row)

# --- TEST ---

log = LogTable()

log.insert_row({"message": "User logged in", "level": "INFO"})

print(f"Table: {log.table_name}")
print(f"Rows: {log.select_all()}")

