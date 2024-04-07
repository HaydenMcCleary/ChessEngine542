import csv

# Define a function to parse the FEN position
def parse_fen(fen_string):
    return fen_string.split(',')

# Define a function to parse the line of moves
def parse_moves(move_string):
    return move_string.split(',')

# Read the CSV file
csv_file = 'training_set/training_data1.csv' 
positions = []

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists
    for row in reader:
        fen_position = row[0]
        line_of_moves = row[1]
        evaluation_score = row[2]
        if evaluation_score.isdigit():  # Check if the evaluation score is a number
            evaluation_score = int(evaluation_score)
        else:
            evaluation_score = 0  # If it's not a number, set it to 0 or handle it as needed
        positions.append({
            'FEN Position': parse_fen(fen_position),
            'Line of Moves': parse_moves(line_of_moves),
            'Evaluation Score': evaluation_score
        })








