import os

def clean_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        cleaned_line = line.rsplit(',', 1)[0]  # Remove everything after the last comma
        cleaned_lines.append(cleaned_line)

    with open(output_file, 'w') as f:
        f.write('\n'.join(cleaned_lines))

# Usage example:

for i in range (1, 670):
    input_file = f"training_set/black/output_file_{i}.csv"
    output_file = f"training_set/black/output_file_{i}_nocp.csv"
    clean_csv(input_file, output_file)
    print("CSV file cleaned and saved as", output_file)
    os.remove(input_file)  # Delete the input file after processing
