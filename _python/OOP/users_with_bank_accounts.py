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

class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = bank_account(0, 0.005)
        self.savings = bank_account(0, 0.02)
    def make_deposit(self, amount, accType):
        if accType == 0:
            self.checking.deposit(amount)
        elif accType == 1:
            self.savings.deposit(amount)
        return self
    def make_withdrawal(self, amount, accType):
        if accType == 0:
            self.checking.withdraw(amount)
        elif accType == 1:
            self.savings.withdraw(amount)
        return self
    def display_user_balance(self, accType):
        if accType == 0:
            print("checking balance is:")
            self.checking.display_account()
        elif accType == 1:
            print("savings account balance is:")
            self.savings.display_account()
        return self

aaron = user("Aaron Fennig", "awfennig@gmail.com").make_deposit(500,1).make_withdrawal(200,1).display_user_balance(1)
aaron = user("Aaron Fennig", "awfennig@gmail.com").make_deposit(500,0).make_withdrawal(200,0).display_user_balance(0)
aaron.make_deposit(500, 1)
aaron.display_user_balance(1)