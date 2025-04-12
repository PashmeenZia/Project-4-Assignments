import time  

# 🎯 3x3 board created using a list
board = [" " for _ in range(9)]  

# 📌 Function to display the board
def print_board():
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("\n")

# 🎯 Function to check if a player has won
def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# 🎯 Function to take a player's move
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1-9.")

# 🎮 Main game loop
def play_game():
    print("\n🎉 Welcome to Tic-Tac-Toe! 🎉")
    print_board()
    current_player = "X"
    
    for turn in range(9):
        player_move(current_player)
        print_board()
        
        if check_winner(current_player):
            print(f"🎉 Player {current_player} wins! 🎉")
            return
        
        current_player = "O" if current_player == "X" else "X"  # Switch player
        time.sleep(1)  # ⏳ Small delay for better experience

    print("😲 It's a draw! No one wins. 😲")

# 🚀 Start the game
if __name__ == "__main__":
    play_game()