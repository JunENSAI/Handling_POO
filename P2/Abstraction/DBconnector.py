from abc import ABC, abstractmethod

class DBconnector(ABC):
    
    @abstractmethod
    def connect(self):
        """Establish connection to DB"""
        pass

    @abstractmethod
    def disconnect(self):
        """Close connection"""
        pass

class Postgres(DBconnector):
    def connect(self):
        print("Connecting to Postgres...")
    
    def disconnect(self):
        print("Closing Postgres...")

db = Postgres()
db.connect()