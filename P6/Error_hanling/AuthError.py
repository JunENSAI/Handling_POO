class AuthError(Exception):
    pass

class InvalidUsernameError(AuthError):

    pass

class InvalidPasswordError(AuthError):

    pass

def login(username: str, password: str):
    if username != "admin":
        raise InvalidUsernameError("User does not exist")

    if password != "secret":
        raise InvalidPasswordError("Wrong password")
    
    return True

try:
    login("admin", "wrongpass")
except InvalidPasswordError as e:
    print(f"Access denied: {e}")