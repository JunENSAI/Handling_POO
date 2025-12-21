import psycopg2

class Database:

    _instance = None

    def __init__(self):
        if not hasattr(self, "connection"):
            print("Connecting to Postgres...")
            try:
                self.connection = psycopg2.connect(
                    host="localhost",
                    database="db_poo",
                    user="poo_user",
                    password="poo_train36"
                )
            except Exception as e:
                print(f"Connection Failed: {e}")
    
    def get_connection(self):
        return self.connection

    def __new__(cls):
        """ ensure that only one instance exists """
        if cls._instance is None:
            print("Creating the Database connection")
            cls._instance = super().__new__(cls)
        return cls._instance

