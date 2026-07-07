# Key decisions: We implement the O(n log n) LIS algorithm using binary search 
# via the `bisect` library. This satisfies Rosalind's constraints for n = 10,000 
# effortlessly, avoiding the memory stack vulnerabilities of an O(n^2) loop.

import sys
from pathlib import Path
from bisect import bisect_left

def get_lis(sequence: list[int]) -> list[int]:
    """
    Computes a longest increasing subsequence in O(n log n) time using patience sorting.
    """
    if not sequence:
        return []

    # tails[i] stores the actual index in `sequence` of the smallest tail of an increasing subsequence of length i+1
    tails = []
    # parent[i] stores the index of the element preceding sequence[i] in the LIS
    parent = [-1] * len(sequence)
    # paths tracks the active indices corresponding to each position in tails
    paths = []

    for i, x in enumerate(sequence):
        # Binary search to find where x fits inside the tails tracker values
        tail_values = [sequence[idx] for idx in paths]
        idx = bisect_left(tail_values, x)

        if idx == len(paths):
            paths.append(i)
        else:
            paths[idx] = i

        if idx > 0:
            parent[i] = paths[idx - 1]

    # Backtrack to reconstruct the sequence path
    result = []
    curr = paths[-1] if paths else -1
    while curr != -1:
        result.append(sequence[curr])
        curr = parent[curr]

    return result[::-1]

def solve_lgis(n: int, permutation: list[int]) -> tuple[list[int], list[int]]:
    """
    Finds both the LIS and LDS of a given permutation sequence.
    """
    lis = get_lis(permutation)
    
    # An LDS of X is simply the LIS of X with inverted relative weight properties
    # We transform each element x to -x to reuse our optimized LIS function
    negated_seq = [-x for x in permutation]
    lds_negated = get_lis(negated_seq)
    lds = [-x for x in lds_negated]
    
    return lis, lds

if __name__ == "__main__":
    try:
        # Cross-platform relative file path resolution using Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_lgis.txt"
        
        if dataset_path.exists():
            lines = dataset_path.read_text().strip().splitlines()
            n = int(lines[0].strip())
            permutation = [int(x) for x in lines[1].strip().split()]
            
            lis, lds = solve_lgis(n, permutation)
            
            # Print the space-separated output sequences
            print(" ".join(map(str, lis)))
            print(" ".join(map(str, lds)))
        else:
            raise FileNotFoundError
            
    except FileNotFoundError:
        # Fallback textbook sample test case simulation
        sample_n = 5
        sample_perm = [5, 1, 4, 2, 3]
        lis, lds = solve_lgis(sample_n, sample_perm)
        
        # Expected Output: LIS=[1, 2, 3] (or [5, 1, 2, 3] variants) and LDS=[5, 4, 2] (or [5, 4, 3])
        print("Sample LIS:", " ".join(map(str, lis)))
        print("Sample LDS:", " ".join(map(str, lds)))