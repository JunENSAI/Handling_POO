import pytest
from Pytest.Wallet import Wallet

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