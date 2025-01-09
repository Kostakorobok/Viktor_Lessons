def welcome_message():
    welcome = """
Instructions:
- This is 2 player game
- Input E to exit the game
"""

def row_column_input():
    row = int(input("Enter the row number (1-3): ")) - 1
    col = int(input("Enter the column number (1-3): ")) - 1
    return row, col
