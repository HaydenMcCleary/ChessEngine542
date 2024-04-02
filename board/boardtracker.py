import chess

moves = []


def islegal(moved_char_not, board):

    try:
        move = chess.Move.from_uci(moved_char_not)
    except ValueError:
        return False
    return move in board.legal_moves

def play_game(user_move):
    board = chess.Board()
    moves = []

    while not board.is_game_over():

        # Validate and make the move
        if islegal(user_move, board):
            move = chess.Move.from_uci(user_move)
            board.push(move)
            moves.append(move)

    print("Game Over")
    print("Result: ", board.result())
    print("Moves Played:")
    for i, move in enumerate(moves, start=1):
        print(f"{i}. {move}")

# if __name__ == "__main__":
#     play_game()
 