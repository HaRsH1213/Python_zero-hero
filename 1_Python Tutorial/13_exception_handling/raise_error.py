class InsufficientFunds(Exception):
    pass

balance=0

def deposit(amount):
    global balance
    if amount<=0:
        raise ValueError("Amount should be positive or greater than zero")
    balance += amount
    print(f"Amount is succesfully deposite")

#print(f"Amount is succesfully deposite {deposit(1)}")
#print(balance)

def withdraw(amount):
    global balance
    if amount > balance:
        raise InsufficientFunds(f"Not enough funds. Current balance {balance}")
    balance -= amount
    print(f"Amount is successfully withdraw. Your Current balance: ",balance)


deposit(100)
deposit(50)
withdraw(500)
print(balance)