# Key decisions: We use Python's built-in string manipulation libraries and array-slicing mechanics
# to calculate reverse complements natively without adding performance overhead. Since the string length
# is bounded tightly at 1,000 bp, a nested sliding window check completes in milliseconds.

import sys
from pathlib import Path
from Bio import SeqIO


def get_reverse_complement(dna_string: str) -> str:
    """
    Computes the reverse complement of a DNA string using an optimized translation table mapping.
    """
    trans_table = str.maketrans("ATCG", "TAGC")
    return dna_string.translate(trans_table)[::-1]


def locate_restriction_sites(dna_sequence: str) -> list[tuple[int, int]]:
    """
    Scans a DNA sequence for reverse palindromes with lengths ranging from 4 to 12.
    Returns a list of tuples containing (1-based start position, length).
    """
    results = []
    seq_len = len(dna_sequence)

    # Outer loop tracks the starting window index boundary
    for i in range(seq_len):
        # Inner loop checks window lengths between 4 and 12 (inclusive)
        for length in range(4, 13):
            # Break early if the window exceeds the remaining length of the string
            if i + length > seq_len:
                break

            substring = dna_sequence[i : i + length]
            rev_comp = get_reverse_complement(substring)

            if substring == rev_comp:
                # Store the 1-based start coordinate along with the current length
                results.append((i + 1, length))

    return results


if __name__ == "__main__":
    try:
        # Cross-platform relative file path resolution using Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_revp.txt"

        if dataset_path.exists():
            record = SeqIO.read(dataset_path, "fasta")
            dna_str = str(record.seq).upper()

            # Execute restriction search parameters
            palindrome_matches = locate_restriction_sites(dna_str)
            for pos, length in palindrome_matches:
                print(f"{pos} {length}")
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        # Fallback textbook sample test case simulation
        sample_dna = "TCAATGCATGCCTC"
        # Expected Output contains indices matching lengths (e.g., ATGCAT, TGCA)
        sample_matches = locate_restriction_sites(sample_dna)
        print("Sample Run Output ([Start] [Length]):")
        for pos, length in sample_matches:
            print(f"{pos} {length}")
