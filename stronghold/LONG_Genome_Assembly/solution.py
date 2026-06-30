# Key decisions: We use a dynamic list pool approach. Since the dataset size is small 
# (N <= 50), restarting the loop upon finding a match keeps the greedy logic clean and 
# easily traces the unique assembly path without heavy graph overhead.

import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def find_overlap(s1: str, s2: str, min_overlap: int) -> int:
    """
    Returns the length of the maximum overlap where a suffix of s1 matches a prefix of s2.
    Returns 0 if no overlap meets or exceeds min_overlap.
    """
    max_len = min(len(s1), len(s2))
    for length in range(max_len, min_overlap - 1, -1):
        if s1[-length:] == s2[:length]:
            return length
    return 0

def assemble_genome(reads: list) -> str:
    """
    Assembles a list of overlapping reads into the shortest common superstring.
    """
    # Use the first read as the foundation for the assembled superstring
    superstring = reads.pop(0)
    min_overlap = (len(superstring) // 2) + 1

    while reads:
        matched_index = None
        for i, read in enumerate(reads):
            # Case 1: The read overlaps at the tail end (suffix) of our superstring
            overlap_len = find_overlap(superstring, read, min_overlap)
            if overlap_len > 0:
                superstring += read[overlap_len:]
                matched_index = i
                break
                
            # Case 2: The read overlaps at the front end (prefix) of our superstring
            overlap_len = find_overlap(read, superstring, min_overlap)
            if overlap_len > 0:
                superstring = read[:-overlap_len] + superstring
                matched_index = i
                break
        
        # Remove the successfully merged read from the pool and repeat
        if matched_index is not None:
            reads.pop(matched_index)
            
    return superstring

if __name__ == "__main__":
    from utils.bioutils import parse_fasta
    
    try:
        current_dir = os.path.dirname(__file__)
        dataset_path = os.path.abspath(os.path.join(current_dir, "..", "Dataset", "rosalind_long.txt"))
        
        fasta_dict = parse_fasta(dataset_path)
        reads_pool = list(fasta_dict.values())
        
        assembled_sequence = assemble_genome(reads_pool)
        print(assembled_sequence)
            
    except FileNotFoundError:
        # Fallback minimal sample test case matching Rosalind specification
        sample_reads = [
            "ATTAGACCTG",
            "CCTGCCGGAA",
            "AGACCTGCCG",
            "GCCGGAATAC"
        ]
        print(assemble_genome(sample_reads))
