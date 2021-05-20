class User:    # here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer_money(self, transferee, amount):
        self.make_withdrawal(amount)
        transferee.make_deposit(amount)
        print(self.account_balance)
        print(transferee.account_balance)
        return self

Mario = User("Mario", "itsame@8bit.nes")
Luigi = User("Luigi", "player2@8bit.nes")
Aaron = User("Aaron", "puppetmaster@8bit.nes")

Mario.make_deposit(20).make_deposit(20).make_deposit(100).make_withdrawal(50).display_user_balance()
Luigi.make_deposit(70).make_deposit(500).make_deposit(70).make_withdrawal(75).make_withdrawal(75).display_user_balance().transfer_money(Mario, 90)
Aaron.make_deposit(5000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(500).display_user_balance()