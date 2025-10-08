# Pseudocode:

# Begin
# Print the game board
# Prepare nested Array to store the game
# Aking player to choose X or O
# Start game loop (9 rounds)
    # Asking player X for a field
    # Check: Is field already taken and if the field is inside of the game board (using numberCheck array)
        # If check failed asking player X again for a field
        # If check was successful place X on the field
    # Check: Did player X wins
        # Check the winning combination
            # If player wins, stop loop
            # If not continue
        # If the player didn't win continue
    # Computer makes a random move
    # Check: Is field already taken and if the field is inside of the game board (using numberCheck array)
        # If check failed asking computer X again for a field
        # If check was successful place X on the field
    # Check if computer wins
        # If computer wins, stop loop
        # If not continue
    # Checking for a free number
# End of loop
# Printing winning, draw or loosing message
# Asking user to play again

#   X | X | X
#   4 | 5 | 6
#   7 | 8 | 9

# win combinations:

# numberCheck = [X,2,3,4,5,6,7,8,9]

# one = null
# two = null



# one == two & one == three
# one == four & one == seven

# X +- 1
# X +- 2 
# X +- 3
# X +- 4

# Functions we need:
# print_board() Liam
# check_win() Malte
# check_draw()
# player_move() Liam
# computer_move() Liam
# check_valid_move()
# reset_game()
# player_choose_xor_o() Ehsan

import os
import random

winningCombinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[3,6,9],[1,5,9],[2,5,8],[3,5,7]]

def check_win():
    for comb in winningCombinations:
        a,b,c = combo
        if board[a] == board[b] == board[c] and board[a] in ("X", "O"):
            return True
    return False

def validate_move(field):
    if field < 1 or field > 9:
        return False
    if field in board:
        return True
    return False

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, len(board), 3):
        print(' | '.join(str(x) for x in board[i:i+3]))
        if i < 6:
            print('---------')

def player_move():
    move = input("Your move: ")
    print("\033[A\033[K", end="")
    return move

def comp_move():
    return random.randint(1, 9)

print_board(board)
