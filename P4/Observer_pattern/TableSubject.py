class TableSubject:
    def __init__(self):
        self._observers = []
        self._storage = []

    def attach(self, observer_func):
        self._observers.append(observer_func)

    def notify(self, data):
        for observer in self._observers:
            observer(data)

    def insert(self, row:dict):
        self._storage.append(row)
        print("Row inserted.")
        self.notify(row)
        

def send_email(row):
    print(f"Sending email to {row['name']}...")

# Usage
tbl = TableSubject()
tbl.attach(send_email)

tbl.insert({"name": "Alice"})