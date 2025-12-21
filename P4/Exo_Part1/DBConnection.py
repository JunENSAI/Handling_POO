class DBConnection:

    _instance = None

    def __init__(self):
        self.status = "Connected"

    def __new__(cls):
        """ ensure that only one instance exists """
        if cls._instance is None:
            print("Creating the Database connection")
            cls._instance = super().__new__(cls)
        return cls._instance

class ModelFactory:

    @staticmethod
    def create_model(model_type):
        if model_type == "user":
            return "User Model Created"
        elif model_type == "product":
            return "Product Model Created"
        else:
            raise ValueError("Unknows Model type")

conn1 = DBConnection()
conn2 = DBConnection()

print(conn1 is conn2)

user_md = ModelFactory.create_model("user")

print(user_md)