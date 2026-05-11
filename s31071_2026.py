import random

def generate_sequence (length: int) -> str:
    """Returns a random DNA sequence of the specified length."""
    nucleotides = ['A', 'G', 'C', 'T']
    return ''.join(random.choice(nucleotides) for i in range(length))

def calculate_stats (sequence: str) -> dict :
    """Returns a dictionary of sequence statistics.
Keys: "A", "C", "G", "T" ( float values , %),
           "GC" ( float value , %)."""
    total = len(sequence)
    stats = {}
    for nuc in ['A', 'C', 'G', 'T']:
        stats[nuc] = (sequence.count(nuc) / total) * 100
    stats['GC'] = stats['G'] + stats['C']
    return stats

def insert_name (sequence: str, name: str) -> str:
    """Inserts a name at a random position in the sequence.
Name written in lowercase letters."""
    position = random.randint(0, len(sequence))
    return sequence[:position] + name.lower() + sequence[position:]

def format_fasta ( seq_id : str , description : str ,
                 sequence: str, line_width : int = 80) -> str:
    """Returns a formatted FASTA record as a string."""
    header = ">" + seq_id
    if description:
        header = header + " " + description

    result = header + "\n"
    for i in range(0, len(sequence), line_width):
        line = sequence[i:i + line_width]
        result = result + line + "\n"
    return result

def validate_positive_int (prompt: str,
                          min_val : int = 1,
                          max_val : int = 100_000) -> int:
    """Gets an integer from the user in a range.
In case of an error, repeats the question."""
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Error: value must be an integer in the range [{min_val}, {max_val}].")
        except ValueError:
            print(f"Error: value must be an integer in the range [{min_val}, {max_val}].")

def main():
    """You know."""

if __name__ == "__main__":
    main()

