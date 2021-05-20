class bank_account:
    def __init__(self, amount, interest_rate = 0.01):
        self.balance = amount
        self.interest_rate = interest_rate
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if(self.balance <= 0):
            print("Insufficient Funds")
            self.balance += amount -5
        return self
    def display_account(self):
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.interest_rate
        return self

aaron = bank_account(0)
rick = bank_account(0)
aaron.deposit(100).deposit(200).deposit(50).withdraw(150).yield_interest().display_account()
aaron.withdraw(500)
aaron.display_account()
rick.deposit(25).deposit(700).withdraw(300).withdraw(20).withdraw(100).withdraw(150).yield_interest().display_account()