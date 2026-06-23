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
    
    with open(file_path) as file:
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


def find_motif_indices(s: str, motif: str) -> list:
    """
    Finds all 1-based starting positions of a motif substring within a main string.
    Accounts for overlapping occurrences.
    """
    positions = []
    s_len = len(s)
    m_len = len(motif)
    
    # Slide a window of the motif's length across the main sequence
    for i in range(s_len - m_len + 1):
        if s[i:i+m_len] == motif:
            positions.append(i + 1)  # Convert 0-based index to 1-based
            
    return positions

# Complete RNA Codon Table
RNA_CODON_TABLE = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

def translate_rna_to_protein(rna: str) -> str:
    """
    Translates an RNA string into a protein string using the standard genetic code.
    Stops translation when a 'Stop' codon is encountered.
    """
    rna_upper = rna.upper().strip()
    protein = []
    
    # Process the RNA string in chunks of 3 (codons)
    for i in range(0, len(rna_upper), 3):
        codon = rna_upper[i:i+3]
        
        # Ensure we have a complete 3-letter codon
        if len(codon) < 3:
            break
            
        amino_acid = RNA_CODON_TABLE.get(codon, '')
        
        if amino_acid == 'Stop':
            break
        elif amino_acid:
            protein.append(amino_acid)
            
    return "".join(protein)

# Complete mass_table
mass_table = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'L': 113.08406,
        'K': 128.09496,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
    }

def calculate_protein_mass(protein_string:str):
    
    total_mass = 0.0
    
    clean_string = "".join(protein_string.split())
    
    for aa in clean_string:
        if aa in mass_table:
            total_mass += mass_table[aa]
        else:
            print(f"Warning: Character {aa} is not a valid amino acid.")
            
    return round(total_mass, 3)