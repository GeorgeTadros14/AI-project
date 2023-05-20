from board import Board
from Alphabeta import alphabeta
from MiniMax import minimax
import time
import random

# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        # YOUR CODE GOES HERE

        # Call the alphabeta function to select the best move
        column, _ = alphabeta(board, depth=5, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)
        board.select_column(column)

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        random_column = random.randint(0, 6)
        board.select_column(random_column)

        time.sleep(2)


if __name__ == "__main__":
    main()
