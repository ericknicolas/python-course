'''
Class Player defines object Player
'''

from hand import Hand
from wallet import Wallet
from bet import Bet

class Player:

    def __init__(self, name, initBalance):
        self.name = name        
        self.hand = Hand()
        self.wallet = Wallet(initBalance)
        self.bet = Bet()
    
    def make_a_bet(self):
        while True:
            try:
                self.bet.amount = int(input(f"\nHi {self.name}, your current balance is {self.wallet.balance}, How many chips you want to play? "))
            except:
                print("\nSorry! but it must be a integer")
            else:
                if(self.bet.amount > self.wallet.balance):
                    print(f"\nSorry! but you only can bet {self.wallet.balance} as maximum")
                else:
                    self.wallet.withdraw(self.bet.amount)
                    break
    
    def is_busts(self):
        return(self.hand.value > 21)

    def __str__(self):
        return f"\n{self.name}"