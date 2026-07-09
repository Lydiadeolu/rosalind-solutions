# Key decisions: We use `math.factorial` to perform the combinatorial multiplication
# directly in O(N) time. This eliminates the need to build an explicit graph structure.
# Paths are resolved safely using cross-platform `pathlib`.

import sys
import math
from pathlib import Path
from Bio import SeqIO


def count_perfect_matchings(rna_sequence: str) -> int:
    """
    Calculates the number of perfect matchings for an RNA sequence using factorials.
    """
    # Count occurrence instances of one base from each independent pairing set
    count_au = rna_sequence.count("A")
    count_cg = rna_sequence.count("C")

    # Total matchings = (Count of A)! * (Count of C)!
    return math.factorial(count_au) * math.factorial(count_cg)


if __name__ == "__main__":
    try:
        # Cross-platform relative file path resolution using Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_pmch.txt"

        if dataset_path.exists():
            record = SeqIO.read(dataset_path, "fasta")
            rna_str = str(record.seq).upper()

            # Print the total number of perfect matchings
            print(count_perfect_matchings(rna_str))
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        # Fallback textbook sample test case simulation
        sample_rna = "AGCUAGUACACUUUGUGCCUCCAUGUCAUAACCUGAUGAUGAU"
        # Expected Output: 12
        print("Sample Run Output:", count_perfect_matchings("AGCU"))
