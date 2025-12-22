from typing import List, Optional

class User:
    def __init__(self, name: str):
        self.name = name

def get_user_names(users: List[User]) -> List[str]:
    return [u.name for u in users]

def find_user(id: int) -> Optional[User]:
    if id == 1:
        return User("Alice")
    return None

def process_transaction(user: User, amount: float, currency:str="USD") -> bool:
    print(f"User {user.name} spent {amount} {currency}")
    return True