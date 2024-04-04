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
        high_score = 0  # Initialize with negative infinity to ensure the first score is always higher
        best_move = ""
        is_mate = False  # Flag to indicate if mate is detected
        
        for eval_data in line["evals"]:
            for pv in eval_data["pvs"]:
                # Check if mate is detected
                if "mate" in pv:
                    is_mate = True
                    break  # Exit the loop if mate is detected
                # Extract line of moves and evaluation score
                line_moves = pv["line"]
                eval_score = pv.get("cp")
                
                # Check if eval_score is not None before comparing with the high_score
                if eval_score is not None and abs(eval_score) > abs(high_score):
                    high_score = eval_score
                    best_move = line_moves
            
            if is_mate:
                best_move = line_moves
                break  # Exit the loop if mate is detected
        
        # Store the best move and its evaluation score in the dictionary
        data_dict[fen_position] = (best_move, "Mate" if is_mate else high_score)

# Print to check
for fen, (move, score) in data_dict.items():
    print("FEN Position:", fen)
    print("Line of Moves:", move)
    print("Evaluation Score:", score)
    print()
