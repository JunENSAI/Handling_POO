import logging

class Server:

    def __init__(self):
        logging.basicConfig(filename='server.log', level=logging.INFO)
        logging.info("Server Starting")
    
    def connect(self,username:str) -> bool:
        if username!="admin":
            logging.error("Connection Failed")
        return True

s = Server()

s.connect("junior")
