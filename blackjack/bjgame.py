'''
BlackJack game
'''
from deck import Deck

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

deck = Deck(suits, ranks)
deck.shuffle()
print(deck)