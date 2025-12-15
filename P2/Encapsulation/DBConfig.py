class DBConfig:
    def __init__(self):
        self.public_host = "localhost"
        self._port = 5432
        self.__password = "secret_pass"

    def verify_connection(self):
        print(f"Connecting to {self.public_host}:{self._port} using {self.__password}")

config = DBConfig()

# 1. Accessing Public (Works fine)
print(f"Public: {config.public_host}")

# 2. Accessing Protected
print(f"Protected: {config._port}")

# 3. Accessing Private (WILL FAIL)
try:
    print(config.__password)
except AttributeError as e:
    print(f"FAILED: {e}")

# 4. The Hack (Name Mangling) : Python renames __password to _DatabaseConfig__password
print(f"Hacked: {config._DBConfig__password}")

print(config.verify_connection()) #why self.__password works here : Because within the class, Python allows access to private attributes directly.