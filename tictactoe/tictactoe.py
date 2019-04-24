board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
#board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def printBoard(board):
    print("\n" + f"| {board[6]} " + f"| {board[7]} " + f"| {board[8]} |")
    print("-------------")
    print(f"| {board[3]} " + f"| {board[4]} " + f"| {board[5]} |")
    print("-------------")
    print(f"| {board[0]} " + f"| {board[1]} " + f"| {board[2]} |" + "\n")

printBoard(board)