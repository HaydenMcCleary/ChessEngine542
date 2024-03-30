import jsonlines

# Path to your JSONL file
file_path = "training_data/output_1.jsonl"

# Lists to store extracted data
fen_positions = []
lines_of_moves = []
evaluation_scores = []

# Open the JSONL file for reading
with jsonlines.open(file_path, "r") as reader:
    # Iterate over each line in the JSONL file
    for line in reader:
        # Extract FEN position for this line
        fen_position = line.get("fen")
        fen_positions.append(fen_position)
        
        # Extract evaluations and associated lines of moves
        for eval_data in line["evals"]:
            for pv in eval_data["pvs"]:
                # Extract line of moves and evaluation score
                line_moves = pv["line"]
                eval_score = pv.get("cp")
                
                # Store line of moves and evaluation score
                lines_of_moves.append(line_moves)
                evaluation_scores.append(eval_score)




# print to check
for fen, line, score in zip(fen_positions, lines_of_moves, evaluation_scores):
    print("FEN Position:", fen)
    print("Line of Moves:", line)
    print("Evaluation Score:", score)
    print()