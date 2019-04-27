#board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
playerOne = ""
playerTwo = ""

def printBoard(board):
    
    print("\n" + f"| {board[6]} " + f"| {board[7]} " + f"| {board[8]} |")
    print("-------------")
    print(f"| {board[3]} " + f"| {board[4]} " + f"| {board[5]} |")
    print("-------------")
    print(f"| {board[0]} " + f"| {board[1]} " + f"| {board[2]} |" + "\n")


def symbolSelection():

    global playerOne
    global playerTwo

    while True:
        playerOne = input("Please choose if you want to play with 'X' symbol or 'O' symbol?: ").upper()

        if(playerOne == "X"):
            playerTwo = "O"
            break
        
        elif(playerOne == "O"):
            playerTwo = "X"
            break

        else:
            print("Not a valid symbol!")


def is_empty(position):
    return (board[position - 1] == " ")


def playerSelection(player):

    while True:
        playerSelection = int(input("Please introduce your slection: "))
        
        if((playerSelection in list(range(1,10))) and (is_empty(playerSelection))):
            board[playerSelection - 1] = player
            break
        else:
            print("Not a valid selection!")
    
    printBoard(board)


def winner():

    return  (
        ((board[0] == board[1] == board[2] != " ") or (board[3] == board[4] == board[5] != " ") or (board[6] == board[7] == board[8] != " ")) or 
        ((board[0] == board[3] == board[6] != " ") or (board[1] == board[4] == board[7] != " ") or (board[2] == board[5] == board[8] != " ")) or
        ((board[0] == board[4] == board[8] != " ") or (board[6] == board[4] == board[2] != " ")))


def game():

    turn = playerOne
    
    while not winner():
        playerSelection(turn)

        if(turn == playerOne):
            turn = playerTwo
        else:
            turn = playerOne

    print("We have a winner!")    

symbolSelection()
game()