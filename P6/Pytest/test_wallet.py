import pytest

class Wallet:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough money")
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(5)
    assert wallet.balance == 15 #try 16 and you saw that part will fail 

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend(10)
    assert wallet.balance == 10

def test_wallet_spend_too_much():
    wallet = Wallet(5)
 
    with pytest.raises(ValueError):
        wallet.spend(100)