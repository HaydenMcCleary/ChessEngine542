import numpy as np
import pandas as pd
import numpy as np
import chess
import csv

def fen_to_matrix(fen_str):
    # Initialize an empty 8x8 matrix
    board_matrix = np.zeros((8, 8), dtype=int)

    # Parse the FEN string
    board = chess.Board(fen_str)

    # Map piece types to numerical values
    piece_values = {
    'p': 1, 'P': -1, 'n': 2, 'N': -2, 'b': 3, 'B': -3, 'r': 4, 'R': -4,
    'q': 5, 'Q': -5, 'k': 6, 'K': -6
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
    positions = []
    moves = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            fen = row[0]
            move_list = row[1]
            positions.append(fen_to_matrix(fen))
            moves.append(move_list)  # Append moves without conversion
    return positions, moves

# Example usage
positions, moves = convert_csv_to_numeric('training_set/small_test.csv')

# Print the positions and moves
for i in range(len(positions)):
    print("Position:")
    print(positions[i])
    print("Moves:")
    print(moves[i])
    print("-----------------")
