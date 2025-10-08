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
# print_board() Liam ✅
# check_win() Malte ✅
# check_draw() Malte ✅
# player_move() Liam ✅
# computer_move() Liam ✅
# check_valid_move() Malte ✅
# reset_game() Liam ✅
# player_choose_xor_o() Ehsan
# main_game_loop() Malte ✅
# win count for player and computer Liam ✅

import os
import random

# Global variables
initial_board = list(range(1, 10))
board = initial_board.copy()
winning_combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[3,6,9],[1,5,9],[2,5,8],[3,5,7]]
player_symbol = "X"
computer_symbol = "O"
p_win = 0
c_win = 0

def check_win():
    for comb in winning_combinations:
        a, b, c = comb
        if board[a-1] == board[b-1] == board[c-1] and board[a-1] in ("X", "O"):
            return board[a]
    return None

def check_draw() -> bool:
    return all(not isinstance(x, int) for x in board)

def validate_move(field):
    if field < 1 or field > 9:
        return False
    if field in board:
        return True
    return False

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\nTic-Tac-Toe\n")
    for i in range(0, len(board), 3):
        print(' | '.join(str(x) for x in board[i:i+3]))
        if i < 6:
            print('-' * 9)
    print()

def player_move():
    while True:
        try:
            move = int(input("Your move (1–9): "))
            if validate_move(move):
                board[move - 1] = player_symbol
                print_board(board)
                break
            else:
                print("Invalid move! Field already taken or out of range.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

def computer_move():
    free_fields = [x for x in board if isinstance(x, int)]
    if not free_fields:
        return
    move = random.choice(free_fields)
    board[move - 1] = computer_symbol
    print_board(board)

def reset_board():
    board[:] = initial_board


def player_choose_xor_o():
    global player_symbol, computer_symbol
    while True:
        choice = input("Choose your symbol (X/O): ").upper()
        if choice in ['X', 'O']:
            player_symbol = choice
            computer_symbol = 'O' if choice == 'X' else 'X'
            break
        else:
            print("Invalid choice! Please choose X or O.")
            
if __name__ == "__main__":
    while True:
        # 1) ask symbol before each game
        player_choose_xor_o()
        print_board(board)

        # 2) who starts?
        current = "player" if player_symbol == "X" else "computer"

        while True:
            if current == "player":
                player_move()
                winner = check_win()
                if winner:
                    print("Player wins!")
                    p_win += 1
                    break
                if check_draw():
                    print("It's a draw.")
                    break
                current = "computer"
            else:
                computer_move()
                winner = check_win()
                if winner:
                    print("Computer wins!")
                    c_win += 1
                    break
                if check_draw():
                    print("It's a draw.")
                    break
                current = "player"

        # 3) scoreboard
        print(f"Score - Player: {p_win}, Computer: {c_win}")

        # 4) reset or exit
        reset = input("Play again? (y/n): ").strip().lower()
        if reset != "y":
            break
        reset_board()



