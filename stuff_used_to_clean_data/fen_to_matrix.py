import numpy as np
import csv
import chess

# Function to convert FEN string to a numerical representation
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
    file_mapping = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8
    }

    positions = []
    moves = []
    FEN_positions = []
    legal_moves = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            fen = row[0]
            FEN_positions.append(fen)
            legal_moves.append(num_possible_moves(fen))
            move_list = row[1]
            converted_move_list = ''.join([str(file_mapping[char]) if char in file_mapping else char for char in move_list])
            positions.append(fen_to_matrix(fen))
            moves.append(converted_move_list)  # Append moves without conversion
    
    # Convert lists to NumPy arrays
    positions = np.array(positions)
    moves = np.array(moves)
    legal_moves = np.array(legal_moves)
    
    return positions, moves, FEN_positions, legal_moves

# Function to calculate the number of legal moves for a given FEN position
def num_possible_moves(FEN):
    board = chess.Board(FEN)
    legal_moves = list(board.legal_moves)
    return legal_moves

# Example usage
# positions, moves, FEN_positions, legal_moves = convert_csv_to_numpy('../training_set/small_test.csv')
