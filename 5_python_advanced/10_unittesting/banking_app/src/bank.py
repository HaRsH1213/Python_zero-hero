class Bank:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,Amount):
        if Amount<=0:
            raise ValueError("Amount should be positive or grater than zero")
        self.balance += Amount
        return f"Amount of {Amount} is successfully deposit into your account, Your Current balance: {self.balance}"

    def withdraw(self,Amount):
        if Amount>self.balance:
            raise ValueError(f"Insufficient account balance. Your Current balance: {self.balance}")
        self.balance -= Amount
        return f"Amount of {Amount} is successfully withdrawn. Yor Current balance: {self.balance} "

    def get_balance(self):
        return self.balance




if __name__=='__main__':
    bank=Bank('Harsh')
    print(bank.get_balance())
    print(bank.deposit(50000))
    print(bank.withdraw(10000))
    print(bank.get_balance())

