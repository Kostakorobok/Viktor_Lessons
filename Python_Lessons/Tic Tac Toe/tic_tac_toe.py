# Tic Tac Toe game

from tic_tac_toe_functions import row_column_input
from tic_tac_toe_functions import welcome_message


game_on = True

logo = """
 _____ _        _____            _____           
|_   _(_)      |_   _|          |_   _|          
  | |  _  ___    | | __ _  ___    | | ___   ___  
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \ 
  | | | | (__    | | (_| | (__    | | (_) |  __/ 
  \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|
                                                                               
"""
print(logo)
print(welcome_message())

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

for i in board:
    print(" | ".join(i))
    print("-" * 9)
print("\n")

while (game_on):

    print("Player 1 (X) tern\n")
    row, col = row_column_input()
    board[row][col] = "X" 
    for i in board:
        if i[0] == i[1] == i[2] and i[0] != " ": 
            print("Player 1 wins\n")
            game_on = False
            break
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            print("Player 1 wins\n")
            game_on - False
            break

    for i in board:
        print(" | ".join(i))
        print("-" * 9)

    print("Player 2 (O) tern\n")
    row, col = row_column_input()
    board[row][col] = "O" 
    for i in board:
        if i[0] == i[1] == i[2] and i[0] != " ": 
            print("Player 2 wins\n")
            break

    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    
    continue

    


