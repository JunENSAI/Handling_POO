class DataBase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Database connection for the first time...")
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
db1 = DataBase()
db2 = DataBase()

print(db1 is db2)