'''
BlackJack game
'''
import os
from game import Game

#clear screen
os.system("clear")

game = Game()
game.start()
print(game)

while game.player_turn:
    game.hit_or_stand()

if not game.player.is_busts():
    game.computer_turn()
    print(game)

    if(game.dealer.hand.value > 21):
        print("computer busts!\n")

    elif(game.player.hand.value > game.dealer.hand.value):
        print("you win!\n")
        
    
    elif(game.player.hand.value < game.dealer.hand.value):
        print("you lose!\n")
    
else:
    print("player busts!")