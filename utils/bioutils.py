def count_nucleotides(dna: str) -> dict:
    """
    Counts the occurrences of each nucleotide in a DNA string.
    Returns a dictionary with keys 'A', 'C', 'G', and 'T'.
    """
    dna_upper = dna.upper()  # Standardize to uppercase to avoid case issues
    return {
        'A': dna_upper.count('A'),
        'C': dna_upper.count('C'),
        'G': dna_upper.count('G'),
        'T': dna_upper.count('T')
    }

def transcribe_dna_to_rna(dna: str) -> str:
    """
    Transcribes a DNA string into its corresponding RNA string
    by replacing all occurrences of Thymine ('T') with Uracil ('U').
    """
    return dna.upper().replace('T', 'U')

def reverse_complement(dna: str) -> str:
    """
    Returns the reverse complement of a DNA string.
    Pairs: A<->T, C<->G. The sequence is also reversed.
    """
    dna_upper = dna.upper()
    # Create a translation table mapping bases to their complements
    trans_table = str.maketrans("ATCG", "TAGC")
    # Translate the string, then use slicing [::-1] to reverse it
    return dna_upper.translate(trans_table)[::-1]

def parse_fasta(file_path: str) -> dict:
    """
    Manually parses a multi-sequence FASTA file.
    Returns a dictionary mapping headers (without '>') to their complete sequences.
    """
    sequences = {}
    current_header = None
    
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                current_header = line[1:]
                sequences[current_header] = []
            else:
                if current_header is not None:
                    sequences[current_header].append(line)
                    
    return {header: "".join(chunks) for header, chunks in sequences.items()}


def calculate_gc_content(dna: str) -> float:
    """
    Calculates the GC-content percentage of a given DNA string.
    """
    if not dna:
        return 0.0
    dna_upper = dna.upper()
    g_count = dna_upper.count('G')
    c_count = dna_upper.count('C')
    return ((g_count + c_count) / len(dna)) * 100


def hamming_distance(s1: str, s2: str) -> int:
    """
    Calculates the Hamming distance between two strings of equal length.
    Returns the number of positions at which the corresponding symbols are different.
    """
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length to calculate Hamming distance.")
        
    # Use zip() to pair up characters and count mismatches
    return sum(1 for c1, c2 in zip(s1, s2) if c1 != c2)