def ConstBoard(board):
    print("Current State Of Board:\n")
    for i in range(0, 9):
        print("- " if board[i] == 0 else "O " if board[i] == 1 else "X ", end=" " if i % 3 < 2 else "\n")
    print("\n")

def UserTurn(board):
    pos = int(input("Enter X's position from [1...9]: "))
    if board[pos-1] != 0:
        print("Wrong Move!!!")
        exit(0)
    board[pos-1] = -1

def a_star(board, player):
    x = analyzeboard(board)
    if x != 0:
        return x * player
    pos, value = -1, -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -a_star(board, player*-1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    return 0 if pos == -1 else value

def CompTurn(board):
    pos, value = -1, -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -a_star(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    board[pos] = 1

def analyzeboard(board):
    cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(0, 8):
        if board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] == board[cb[i][2]]:
            return board[cb[i][2]]
    return 0

def main():
    board = [0] * 9
    print("Computer: O Vs. You: X")
    player = int(input("Enter to play 1(st) or 2(nd): "))
    for i in range(0, 9):
        if analyzeboard(board) != 0:
            break
        if (i + player) % 2 == 0:
            CompTurn(board)
        else:
            ConstBoard(board)
            UserTurn(board)
    x = analyzeboard(board)
    ConstBoard(board)
    print("DRAW !" if x == 0 else "YOU WON !" if x == -1 else "YOU LOST !")

main()


# The given code is an implementation of the Tic-Tac-Toe game using the A* search algorithm. 
# Let's go through the code step by step:

# 1. `ConstBoard(board)`: This function prints the current state of the Tic-Tac-Toe board. It
#  iterates through the board list and prints the corresponding symbol for each position: "-" 
#  for empty, "O" for computer (AI), and "X" for the player.

# 2. `UserTurn(board)`: This function allows the user to make a move. It prompts the user to 
# enter the position (1 to 9) where they want to place their "X" symbol. It checks if the chosen 
# position is empty, and if not, it prints an error message and exits the game.

# 3. `a_star(board, player)`: This function performs the A* search algorithm to determine the 
# best move for the AI player. It recursively evaluates the possible moves on the board. It first
#  checks if the current board state is a winning state or a draw. If so, it returns the 
#  corresponding score (1 for AI win, -1 for player win, 0 for draw) multiplied by the player 
#  value. Otherwise, it explores all possible moves and recursively calls `a_star()` for each 
#  move to evaluate the resulting board states. It returns the value (score) and position of the 
#  best move for the current player.

# 4. `CompTurn(board)`: This function is called when it's the AI's turn to make a move. It finds 
# the best move by calling the `a_star()` function and places the AI's symbol ("O") on the board 
# at that position.

# 5. `analyzeboard(board)`: This function analyzes the current board state to check if there is a 
# winner. It checks all possible winning combinations (rows, columns, and diagonals) to see if all 
# positions in any combination are filled with the same symbol (either "O" or "X"). If a winner is 
# found, it returns the corresponding symbol (1 for "O", -1 for "X"). If there is no winner, it returns
#  0.

# 6. `main()`: This is the main function that controls the flow of the game. It initializes the board
#  as an empty list and prompts the player to choose between playing first or second. It then iterates
#   through the game loop, where each player takes turns making moves. If the game ends (a winner is 
#   found or the board is full), it displays the final board state and the result of the game (draw, 
#   player win, or AI win).

# Overall, the code implements a basic version of Tic-Tac-Toe where the AI player uses the A* search
#  algorithm to make intelligent moves.