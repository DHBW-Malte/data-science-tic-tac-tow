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

import os

nestedCombinations = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [3,6,9],
    [1,5,9],
    [2,5,8],
    [3,5,7]
    ]

grid = {
    "one": [None, 1],
    "two": [None, 2],
    "three": [None, 3],
    "four": [None, 4],
    "five": [None, 5],
    "six": [None, 6],
    "seven": [None, 7],
    "eight": [None, 8],
    "nine": [None, 9]
}

board = [
    [grid["one"], grid["two"], grid["three"]],
    [grid["four"], grid["five"], grid["six"]],
    [grid["seven"], grid["eight"], grid["nine"]]
]

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    rows = [' | '.join(str(cell[1]) for cell in row) for row in board]
    print('\n---------\n'.join(rows))

print_board(board)
