import numpy as np
import pandas as pd
import numpy as np
import chess

def fen_to_matrix(fen_str):
    # Initialize an empty 8x8 matrix
    board_matrix = np.zeros((8, 8), dtype=int)

    # Parse the FEN string
    board = chess.Board(fen_str)

    # Map piece types to numerical values
    piece_values = {
    'p': 1, 'P': 2, 'n': 3, 'N': 4, 'b': 5, 'B': 6, 'r': 7, 'R': 8,
    'q': 9, 'Q': 10, 'k': 11, 'K': 12
    }

    # Fill the matrix with piece values
    for rank in range(8):
        for file in range(8):
            square = chess.square(file, rank)
            piece = board.piece_at(square)
            if piece:
                board_matrix[rank, file] = piece_values[piece.symbol()]

    return board_matrix

# Function to read CSV file and convert data to numerical representations
def convert_csv_to_numeric(filename):
    data = pd.read_csv(filename, header=None)
    positions = []
    moves = []
    for i in range(len(data)):
        fen_with_moves = data.iloc[i, 0].split(',')
        fen = fen_with_moves[0]  # Extract FEN position
        move_list = fen_with_moves[1:]  # Extract moves
        positions.append(fen_to_matrix(fen))
        moves.append(move_list)  # Append moves without conversion
    return positions, moves



# Example usage
positions, moves = convert_csv_to_numeric('training_set/small_test.csv')
print(positions)
print(moves)
