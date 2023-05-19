def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return None, board.evaluate()

    valid_moves = board.get_valid_moves()

    if maximizing_player:
        value = float('-inf')
        best_move = None
        for move in valid_moves:
            new_board = board.copy()
            new_board.select_column(move)
            _, new_value = alphabeta(new_board, depth - 1, alpha, beta, False)
            if new_value > value:
                value = new_value
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move, value
    else:
        value = float('inf')
        best_move = None
        for move in valid_moves:
            new_board = board.copy()
            new_board.select_column(move)
            _, new_value = alphabeta(new_board, depth - 1, alpha, beta, True)
            if new_value < value:
                value = new_value
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_move, value