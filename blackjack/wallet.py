'''
Class Wallet defines object Wallet
'''
class Wallet:
    
    def __init__(self, initBalance = 100):
        self.balance = initBalance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def __str__(self):
        return f"\nWallet balance: {self.balance}"
