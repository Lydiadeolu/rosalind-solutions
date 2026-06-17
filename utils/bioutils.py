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