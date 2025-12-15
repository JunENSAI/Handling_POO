class Server:
    
    # CLASS ATTRIBUTE - Shared by all servers
    connected_users = [] 
    
    def __init__(self, port):

        # INSTANCE ATTRIBUTE - Unique to this server
        self.port = port

    def add_user(self, user):
        self.connected_users.append(user)

# Scenario: We have two different servers
server_A = Server(5432)
server_B = Server(8080)

# We add a user ONLY to Server A
server_A.add_user("Alice")

print(f"Server A users: {server_A.connected_users}")
print(f"Server B users: {server_B.connected_users}")

# list is mutable so both servers show the same connected users list, demonstrating the shared nature of class attributes