# Tic Tac Toe game

from tic_tac_toe_functions import row_column_input
from tic_tac_toe_functions import welcome_message
#from tic_tac_toe_function import hor_win
#from tic_tac_toe_function import ver_win
#from tic_tac_toe_function import dia_win

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
    for column in board:
        if column[0] == column[1] == column[2] and column[0] != " ": print("Game Over")

    for i in board:
        print(" | ".join(i))
        print("-" * 9)

    print("Player 2 (O) tern\n")
    row, col = row_column_input()
    board[row][col] = "O" 

    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    
    continue

    


