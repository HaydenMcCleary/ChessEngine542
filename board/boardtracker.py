import chess

# Create a new chess board
board = chess.Board()

def islegal(moved_char_not):

    try:
        move = chess.Move.from_uci(moved_char_not)
    except ValueError:
        return False

    if move in board.legal_moves:
        board.push(move)
        return True
    else:
        return False

# def capturemove():
