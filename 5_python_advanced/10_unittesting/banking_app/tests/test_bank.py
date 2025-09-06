from src.bank import Bank
import pytest

def test_create_account():
    account= Bank('Harsh',50000)
    assert account.owner =="Harsh"
    assert account.balance==50000

def test_deposit():
    account= Bank('Harsh',50000)
    account.deposit(50000)
    account.deposit(50000)
    assert account.balance==150000

def test_withdraw():
    account = Bank('Harsh', 150000)
    with pytest.raises(ValueError):
        account.withdraw(200000000)
    account.withdraw(50000)
    assert account.balance==100000

def test_get_balance():
    account = Bank('Harsh', 150000)

    assert  account.get_balance()==150000
