'''
Class Card defines object Card
'''

class Card:

    def __init__(self, rank, suit):
        self.rank = rank        
        self.suit = suit
        self.visible = True

    def __str__(self):
        if(self.visible):
            return f"{self.rank} of {self.suit}"
        else:
            return "*** HIDEN ***"
