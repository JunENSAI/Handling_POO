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

class Model:

    table_name = ""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def save(self):
        conn = Database().get_connection()
        cursor = conn.cursor()

        try:
            columns = ", ".join(self.__dict__.keys())
            placeholders = ", ".join(["%s"] * len(self.__dict__))
            values = tuple(self.__dict__.values())

            sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, values)

            conn.commit()
        finally:
            cursor.close()

# Tables that must exists on Dbeaver (users , products)
class User(Model):
    table_name = "users"

class Product(Model):
    table_name="products"



if __name__ == "__main__":

    # 1. Create a User
    admin = User(username="admin_alice", role="SuperAdmin")
    admin.save()

    # 2. Create a Product
    laptop = Product(name="Gaming Laptop", price=1299.99)
    laptop.save()

    print("What you observe on Dbeaver") # content is added on table : users and products


