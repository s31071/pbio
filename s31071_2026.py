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

#---------- additional functions ------------
# 1. (3) searches for motif specified by the user (e.g. "ATG") and lists all the positions of occurrences

def search_for_motif(sequence: str, motif: str) -> list:
    positions = []
    for position in range(len(sequence) - len(motif) + 1):
        if sequence[position:position + len(motif)] == motif:
            positions.append(position + 1)
    return positions

# 2. (4) generates and displays the complementary strand and the reverse complementary strand

def complementary(sequence: str) -> str:
    mapping = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement = ''
    for base in sequence:
        if base in mapping:
            complement += mapping[base]
        else:
            complement += base
    return complement

def reverse_complementary(sequence: str) -> str:
    return complementary(sequence[::-1])

#3. (5) generates an mRNA sequence (T to U replacement ) and saves it as a separate record in a FASTA file

def transcribe(sequence: str) -> str:
    return sequence.replace('T', 'U')

def main():
    """You know."""
    length = validate_positive_int("Enter sequence length: ")

    while True:
        seq_id = input("Enter sequence ID: ")
        if seq_id and ' ' not in seq_id:
            break
        print("Error: ID cannot be empty or contain whitespace.")

    description = input("Enter a description of the sequence: ")
    name = input("Enter your name: ")

    sequence = generate_sequence(length)
    sequence_with_name = insert_name(sequence, name)

    fasta_content = format_fasta(seq_id, description, sequence_with_name)
    filename = f"{seq_id}.fasta"

    with open(filename, 'w') as f:
        f.write(fasta_content)

    print(f"Sequence saved to file: {filename}")
    stats = calculate_stats(sequence)

    print(f"Sequence statistics (n={length}):")

    for nuc in ['A', 'C', 'G', 'T']:
        print(f"{nuc}: {stats[nuc]:.2f}%")
    print(f"GC-content: {stats['GC']:.2f}%")

if __name__ == "__main__":
    main()

