# A typical Bank acount

"""
    This class holds the account holder, account balance, an bank name
    A deposit and withdraw module. 
"""

class BankAccount:
    def __init__(self, account_holder, account_balance, bank_name = "Wells Fargo"):
        self.holder = account_holder
        self.balance = account_balance
        self.bank_name = bank_name

    def __str__(self):
        return f"Account Holder: {self.holder}\nAccount Balance: {self.balance}\nBank Name: {self.bank_name}"
    
    def deposit(self, amount):
        self.balance += amount
        print()
        return f"Deposit Successful...\nYour account balance : ${self.balance}" 
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            print()
            return f"Withdraw Successful...\nYour Account balance is: {self.balance}"
        
Account_user_1 = BankAccount("Ozioma Agaecheta", 20000,)
print(Account_user_1)
print(Account_user_1.deposit(100000))
print(Account_user_1.withdraw(100000))
print(Account_user_1.deposit(10000000))