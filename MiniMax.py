import numpy as np

# Define the dimensions of the board
ROWS = 6
COLS = 7

# Define the values for empty and player pieces
EMPTY = 0
PLAYER1_PIECE = 1
PLAYER2_PIECE = 2

# Define the max depth for the minimax algorithm
MAX_DEPTH = 4


def evaluate(board):
    # Check for horizontal wins
    for row in range(ROWS):
        for col in range(COLS - 3):
            window = [board[row][col], board[row][col + 1], board[row][col + 2], board[row][col + 3]]
            if window.count(PLAYER1_PIECE) == 4:
                return 100
            elif window.count(PLAYER2_PIECE) == 4:
                return -100

    # Check for vertical wins
    for row in range(ROWS - 3):
        for col in range(COLS):
            window = [board[row][col], board[row + 1][col], board[row + 2][col], board[row + 3][col]]
            if window.count(PLAYER1_PIECE) == 4:
                return 100
            elif window.count(PLAYER2_PIECE) == 4:
                return -100

    # Check for diagonal wins (positive slope)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row][col], board[row + 1][col + 1], board[row + 2][col + 2], board[row + 3][col + 3]]
            if window.count(PLAYER1_PIECE) == 4:
                return 100
            elif window.count(PLAYER2_PIECE) == 4:
                return -100

    # Check for diagonal wins (negative slope)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            window = [board[row][col], board[row - 1][col + 1], board[row - 2][col + 2], board[row - 3][col + 3]]
            if window.count(PLAYER1_PIECE) == 4:
                return 100
            elif window.count(PLAYER2_PIECE) == 4:
                return -100

    # If no wins, return 0
    return 0

def minimax(board, depth, maximizing_player):
    # Check if the game is over or the max depth has been reached
    score = evaluate(board)
    if score == 100 or score == -100 or depth == MAX_DEPTH:
        return score

    # If not, continue toevaluate the possible moves
    if maximizing_player:
        # Find the maximum score for the available moves
        max_score = -np.inf
        for col in range(COLS):
            # Check if the column is available
            if board[ROWS - 1][col] == EMPTY:
                # Make the move
                row = 0
                while row < ROWS and board[row][col] == EMPTY:
                    row += 1
                board[row - 1][col] = PLAYER1_PIECE

                # Evaluate the move
                score = minimax(board, depth + 1, False)

                # Undo the move
                board[row - 1][col] = EMPTY

                # Update the maximum score
                max_score = max(max_score, score)
        return max_score
    else:
        # Find the minimum score for the available moves
        min_score = np.inf
        for col in range(COLS):
            # Check if the column is available
            if board[ROWS - 1][col] == EMPTY:
                # Make the move
                row = 0
                while row < ROWS and board[row][col] == EMPTY:
                    row += 1
                board[row - 1][col] = PLAYER2_PIECE

                # Evaluate the move
                score = minimax(board, depth + 1, True)

                # Undo the move
                board[row - 1][col] = EMPTY

                # Update the minimum score
                min_score = min(min_score, score)
        return min_score