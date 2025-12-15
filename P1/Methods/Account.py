class Account:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")


acct = Account("User1", 100)
acct.deposit(50)
acct.withdraw(200) # fail because 150 < 200 so insufficient funds
acct.withdraw(20)