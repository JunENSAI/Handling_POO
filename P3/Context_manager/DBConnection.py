class DBConnection:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Enter : Connecting to {self.db_name}...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exit : Closing connection to {self.db_name} automatically.")
        if exc_type:
            print(f"    Error detected: {exc_val}")
        return False 

    def query(self):
        print("    Executing SQL Query...")

with DBConnection("JunioDB") as db:
    db.query()
