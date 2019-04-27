class BankAccount():

    def __init__(self, owner, balance = 0):

        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} done!")

    def withdraw(self, amount):
        
        if(amount > self.balance):
            print(f"Cannot withdraw {amount} because your current balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdraw of {amount} done!")
    
    def __str__(self):
        return(f"Account owner: {self.owner}\nAccount balance: {self.balance}")

acct1 = BankAccount("Jose", 100)
print(acct1)
acct1.deposit(50)
print(acct1)
acct1.withdraw(25)
print(acct1)
acct1.withdraw(200)
    
