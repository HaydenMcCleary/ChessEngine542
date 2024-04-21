import csv
import json

def get_best_line(json_data):
    best_cp = float('-inf')
    best_line = None
    for eval_data in json_data['evals']:
        for pv in eval_data['pvs']:
            if pv['cp'] > best_cp:
                best_cp = pv['cp']
                best_line = pv['line']
    return best_line

def process_jsonl_file(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['FEN', 'Best Line'])
        for line in in_file:
            json_data = json.loads(line.strip())
            fen = json_data['fen']
            best_line = get_best_line(json_data)
            writer.writerow([fen, best_line])

# Replace 'input_file.jsonl' and 'output_file.csv' with your file paths
for i in range (1, 671):
    input_file = f'training_set/output_{i}.jsonl'
    output_file = f'training_set/black/output_file_{i}.csv'
    process_jsonl_file(input_file, output_file)
