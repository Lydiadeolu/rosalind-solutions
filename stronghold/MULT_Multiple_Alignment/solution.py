# Key decisions: 
# 1. 4D DP Tensor initialized using a dictionary keyed by (i, j, k, l) tuples to keep memory footprints clean.
# 2. Itertools.product is used to generate the 15 spatial transition vectors (excluding (0,0,0,0)).
# 3. Standard backtracking tracks the exact transition vector that produced each cell's maximum score.

import sys
from itertools import product
from pathlib import Path

def parse_fasta(fasta_text: str) -> list[str]:
    """Parses raw FASTA format containing exactly four DNA sequences."""
    sequences = []
    current_seq = []
    for line in fasta_text.strip().splitlines():
        if line.startswith(">"):
            if current_seq:
                sequences.append("".join(current_seq))
                current_seq = []
        else:
            current_seq.append(line.strip().upper())
    if current_seq:
        sequences.append("".join(current_seq))
    return sequences

def sum_of_pairs_score(chars: list[str]) -> int:
    """
    Computes the Sum-of-Pairs score for a column of 4 characters.
    Match (including '-' to '-') = 0. Mismatch (or character to '-') = -1.
    """
    score = 0
    # Assess all 6 unique pairs from 4 characters
    for i in range(4):
        for j in range(i + 1, 4):
            if chars[i] != chars[j]:
                score -= 1
    return score

def solve_multiple_alignment(seqs: list[str]):
    # Let L_1, L_2, L_3, L_4 be the lengths of the 4 strings
    L = [len(s) for s in seqs]
    
    # Generate the 15 transitions in 4D space
    # 0 means "Gap introduced" (index stays still), -1 means "Base consumed" (index decrements)
    transitions = list(product([0, -1], repeat=4))
    transitions.remove((0, 0, 0, 0))  # Exclude the stationary state
    
    # DP state tensors
    dp = {}
    backtrack = {}
    
    # Base Case: Origin point
    dp[(0, 0, 0, 0)] = 0
    
    # Fill DP Table iteratively using 4D coordinate space
    for i in range(L[0] + 1):
        for j in range(L[1] + 1):
            for k in range(L[2] + 1):
                for l in range(L[3] + 1):
                    coords = (i, j, k, l)
                    if coords == (0, 0, 0, 0):
                        continue
                    
                    max_score = -float('inf')
                    best_trans = None
                    
                    # Inspect up to 15 possible incoming paths
                    for trans in transitions:
                        prev_coords = (
                            i + trans[0],
                            j + trans[1],
                            k + trans[2],
                            l + trans[3]
                        )
                        
                        # Validate that the incoming path does not exceed grid boundaries
                        if (prev_coords[0] >= 0 and prev_coords[1] >= 0 and 
                            prev_coords[2] >= 0 and prev_coords[3] >= 0):
                            
                            # Determine column characters based on which indices transitioned
                            col_chars = []
                            for idx in range(4):
                                if trans[idx] == -1:
                                    # Consume character from sequence (converting back to 0-based indexing)
                                    col_chars.append(seqs[idx][prev_coords[idx]])
                                else:
                                    # Gap introduced
                                    col_chars.append('-')
                            
                            score = dp[prev_coords] + sum_of_pairs_score(col_chars)
                            if score > max_score:
                                max_score = score
                                best_trans = trans
                                
                    dp[coords] = max_score
                    backtrack[coords] = best_trans

    # Backtracking to reconstruct the aligned sequences
    aligned = ["", "", "", ""]
    curr = (L[0], L[1], L[2], L[3])
    
    while curr != (0, 0, 0, 0):
        trans = backtrack[curr]
        for idx in range(4):
            if trans[idx] == -1:
                aligned[idx] = seqs[idx][curr[idx] - 1] + aligned[idx]
            else:
                aligned[idx] = '-' + aligned[idx]
        
        # Shift coordinate pointer back
        curr = (
            curr[0] + trans[0],
            curr[1] + trans[1],
            curr[2] + trans[2],
            curr[3] + trans[3]
        )
        
    return dp[(L[0], L[1], L[2], L[3])], aligned

if __name__ == "__main__":
    try:
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_mult.txt"
        
        if dataset_path.exists():
            content = dataset_path.read_text()
            seqs = parse_fasta(content)
            
            assert len(seqs) == 4, "This solver requires exactly 4 sequences."
            
            score, alignments = solve_multiple_alignment(seqs)
            print(score)
            for aligned_seq in alignments:
                print(aligned_seq)
        else:
            raise FileNotFoundError
            
    except FileNotFoundError:
        # Fallback textbook sample simulation parameters
        sample_seqs = ["ATATCCG", "TCCG", "ATGTACTG", "ATGTCTG"]
        score, alignments = solve_multiple_alignment(sample_seqs)
        print("Sample Score:", score)
        for seq in alignments:
            print(seq)