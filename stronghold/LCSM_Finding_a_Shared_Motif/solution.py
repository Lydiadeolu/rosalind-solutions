# Key decisions: We implement a Binary Search over the potential motif length 
# coupled with string verification sweeps. This cleanly handles Rosalind's 100-string 
# memory limits efficiently without incurring the massive O(N^K) cost of multidimensional DP.

import sys
from pathlib import Path
from Bio import SeqIO

def common_substring(length: int, shortest_seq: str, other_seqs: list[str]) -> str | None:
    """
    Checks if any substring of the shortest_seq of a given length 
    exists in all other sequences. Returns the motif if found, otherwise None.
    """
    for i in range(len(shortest_seq) - length + 1):
        candidate = shortest_seq[i:i + length]
        if all(candidate in seq for seq in other_seqs):
            return candidate
    return None

def find_longest_common_motif(sequences: list[str]) -> str:
    """
    Executes a Binary Search framework to isolate the longest common substring.
    """
    if not sequences:
        return ""
        
    # Sort sequences to isolate the shortest one for baseline extraction
    sequences = sorted(sequences, key=len)
    shortest_seq = sequences[0]
    other_seqs = sequences[1:]
    
    low, high = 1, len(shortest_seq)
    longest_motif = ""
    
    while low <= high:
        mid = (low + high) // 2
        found_motif = common_substring(mid, shortest_seq, other_seqs)
        
        if found_motif:
            longest_motif = found_motif
            low = mid + 1  # Try to find a longer valid motif
        else:
            high = mid - 1  # Narrow down search to shorter lengths
            
    return longest_motif

if __name__ == "__main__":
    try:
        # Cross-platform relative file path resolution using Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_lcsm.txt"
        
        if dataset_path.exists():
            records = list(SeqIO.parse(dataset_path, "fasta"))
            dna_strings = [str(record.seq) for record in records]
            
            # Print and display the longest common motif sequence
            print(find_longest_common_motif(dna_strings))
        else:
            raise FileNotFoundError
            
    except FileNotFoundError:
        # Fallback textbook sample test case simulation
        sample_data = [
            "GATTACA",
            "TAGACCA",
            "ATACA"
        ]
        # Expected Output: "TA" or "AC"
        print("Sample Run Output:", find_longest_common_motif(sample_data))