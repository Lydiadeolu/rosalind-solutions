# solution.py
# Key decisions: Given the small upper bound constraint (N <= 100 strings), an 
# O(N^2) comparison matrix runs well within fractional seconds. Slicing with [:-3] 
# and [:3] handles the overlap verification step natively.

import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def generate_overlap_graph(fasta_records: dict, k: int = 3) -> list:
    """
    Computes the adjacency list for an overlap graph O_k from a dictionary of FASTA records.
    """
    adjacency_list = []
    
    # Nested loops to check every ordered pair of sequences
    for id_s, seq_s in fasta_records.items():
        for id_t, seq_t in fasta_records.items():
            # Rule 1: Eliminate self-loops
            if id_s == id_t:
                continue
                
            # Rule 2: Check if the suffix of s matches the prefix of t
            suffix_s = seq_s[-k:]
            prefix_t = seq_t[:k]
            
            if suffix_s == prefix_t:
                adjacency_list.append((id_s, id_t))
                
    return adjacency_list

if __name__ == "__main__":
    from utils.bioutils import parse_fasta
    
    try:
        current_dir = os.path.dirname(__file__)
        dataset_path = os.path.abspath(os.path.join(current_dir, "..", "Dataset", "rosalind_grph.txt"))
        
        fasta_data = parse_fasta(dataset_path)
        edges = generate_overlap_graph(fasta_data, k=3)
        
        # Stream the formatted adjacency list out to terminal stdout
        for source, target in edges:
            print(f"{source} {target}")
            
    except FileNotFoundError:
        # Fallback minimal sample test case matching Rosalind specification
        sample_fasta = {
            "Rosalind_0498": "AAATAAA",
            "Rosalind_2391": "AAATTTT",
            "Rosalind_2323": "TTTTCCC",
            "Rosalind_0442": "AAATCCC"
        }
        edges = generate_overlap_graph(sample_fasta, k=3)
        for source, target in edges:
            print(" Data set is not found")
            print(f"{source} {target}")
