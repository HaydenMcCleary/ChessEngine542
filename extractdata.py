import jsonlines

# Path to your JSONL file
file_path = "training_set/output_1.jsonl"

# Dictionary to store extracted data
data_dict = {}

# Open the JSONL file for reading
with jsonlines.open(file_path, "r") as reader:
    # Iterate over each line in the JSONL file
    for line in reader:
        # Extract FEN position for this line
        fen_position = line.get("fen")
        
        # Extract evaluations and associated lines of moves
        eval_moves = []
        for eval_data in line["evals"]:
            for pv in eval_data["pvs"]:
                # Extract line of moves and evaluation score
                line_moves = pv["line"]
                eval_score = pv.get("cp")
                
                # Append line of moves and evaluation score to the list
                eval_moves.append((line_moves, eval_score))
        
        # Store the list of evaluation moves in the dictionary
        data_dict[fen_position] = eval_moves

# Print to check
for fen, eval_moves in data_dict.items():
    print("FEN Position:", fen)
    for move, score in eval_moves:
        print("Line of Moves:", move)
        print("Evaluation Score:", score)
    print()
