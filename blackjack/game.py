'''
Game Wallet defines object Game
'''
from deck import Deck
from player import Player

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

class Game:
    
    def __init__(self):
        self.player = Player("Human", 200)
        self.dealer = Player("Computer", 200)
        self.deck = Deck(suits, ranks)
        self.deck.shuffle()
        self.player_turn = True
    
    def start(self):
        self.player.make_a_bet()
        print(self.player.bet)

        self.player.hand.add_card(self.deck.deal(), True)
        self.player.hand.add_card(self.deck.deal(), True)
        self.dealer.hand.add_card(self.deck.deal(), True)
        self.dealer.hand.add_card(self.deck.deal(), True)
    
    def hit_or_stand(self):
        while True:
            answer = input("\nDou you want Hit or Stand? (push 'h' for Hit and 's' for Stand) ")
            
            if(answer == "h".lower()):
                self.player.hand.add_card(self.deck.deal(), True)
                print(self.player.__str__() + self.player.hand.__str__() + f"\nValue: {self.player.hand.value}")

                
                if(self.player.is_busts()):
                    #print("\nYou busts!")
                    self.player_turn = False
                    break

                else:
                    continue
            
            elif(answer == "s".lower()):
                print(f"{self.player.name} stands... Timer for {self.dealer.name}")
                self.player_turn = False
            
            else:
                print("Please, push 'h' for Hit and 's' for Stand")
                continue
            
            break

    def computer_turn(self):
        while (self.dealer.hand.value < 17):
            self.dealer.hand.add_card(self.deck.deal(), True)
        

    def __str__(self):
        return self.dealer.__str__() + self.dealer.hand.__str__() + f"\nValue: {self.dealer.hand.value}" + "\n" + self.player.__str__() + self.player.hand.__str__() + f"\nValue: {self.player.hand.value}"
