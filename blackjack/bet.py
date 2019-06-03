'''
Class Bet defines object Bet
'''
class Bet:
    
    def __init__(self):
        self.amount = 0
    
    def __str__(self):
        return f"\nBet amount: {self.amount}"