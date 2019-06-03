'''
Class Hand defines object Hand
'''

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces  = 0
    
    def add_card(self, card, visible):
        card.visible = visible
        self.cards.append(card)
        self.value += values[card.rank]

        if(card.rank == "Ace"):
            self.aces += 1
        
        self.adjust_for_aces()

    def adjust_for_aces(self):
        while (self.value > 21) and (self.aces):
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        strcards = ""

        for card in self.cards:
                strcards += card.__str__() + ", "

        return f"\nCards: {strcards}"
