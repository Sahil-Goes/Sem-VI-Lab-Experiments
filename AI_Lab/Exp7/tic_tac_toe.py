#Exp 7: Code to play tic tac toe using python
def print_board(board): 
    print("-" * 13) 
    for row in board: 
        print("| " + row[0] + " | " + row[1] + " | " + row[2] + " |") 
        print("-" * 13) 
 
def check_winner(board): 
    for i in range(3): 
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != " ": 
            return board[i][0] 
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != " ": 
            return board[0][i]   
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ": 
        return board[0][0] 
    if board[0][2] == board[1][1] == board[2][0] != " ": 
        return board[0][2]      

    return None 
 
def is_board_full(board): 
    for row in board: 
        for cell in row: 
            if cell == " ": 
                return False 
    return True 

# Initialize empty board
board = [[" " for _ in range(3)] for _ in range(3)] 
current_player = "X" 

# Game loop
while True: 
    print_board(board) 
    print("Player " + current_player + ", enter your move (row and column): ") 

    try:
        row = int(input("Row (0, 1, or 2): ")) 
        col = int(input("Column (0, 1, or 2): ")) 
    except ValueError:
        print("Please enter valid numeric input.")
        continue

    if row < 0 or row > 2 or col < 0 or col > 2: 
        print("Invalid input! Please enter numbers between 0 and 2.") 
        continue 
     
    if board[row][col] != " ": 
        print("Cell already taken! Try again.") 
        continue 
     
    board[row][col] = current_player 
    winner = check_winner(board) 

    if winner: 
        print_board(board) 
        print("Player " + winner + " wins!") 
        break 

    if is_board_full(board): 
        print_board(board) 
        print("It's a draw!") 
        break 

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

