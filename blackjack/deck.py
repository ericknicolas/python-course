'''
Class Deck defines object Deck
'''
import random
from card import Card

class Deck:

    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.deck = []

        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(rank, suit))
    
    def __str__(self):
        strdeck = ""
        
        for card in self.deck:
            strdeck += "\n" + card.__str__()
        
        return ("The deck has: \n" + strdeck)
    
    def shuffle(self):
        random.shuffle(self.deck)
