# Create classes for a bank account, including functionalities like 
# deposit, withdraw, and balance inquiry.
class BankAccount:
    def __init__(self,account_number,account_holder,initial_balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=initial_balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(f"withdraw ${amount:.2f}. New balance is ${self.balance:.2f}.")
            else:
                print("Insufficient fundsfor this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")
    def get_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance
account=BankAccount("123456789","Rupankar Das",1000)
account.get_balance()
account.deposit(500)
account.withdraw(200)
account.get_balance()
account.withdraw(1500)