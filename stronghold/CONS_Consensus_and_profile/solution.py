# Key decisions: Using a dictionary of lists for the profile matrix maps cleanly 
# to the required output format. This structure enables clear O(N) column scanning 
# where N is the total number of bases across all sequences.

import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def generate_consensus_and_profile(dna_sequences: list) -> tuple:
    """
    Constructs the profile matrix and identifies the consensus sequence
    from a list of equal-length DNA string records.
    """
    seq_length = len(dna_sequences[0])
    
    # Initialize the 4xN profile matrix dictionary
    profile = {
        'A': [0] * seq_length,
        'C': [0] * seq_length,
        'G': [0] * seq_length,
        'T': [0] * seq_length
    }
    
    # Populate frequency coordinates
    for seq in dna_sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1
            
    # Derive consensus string by finding the argmax of each column position
    consensus_list = []
    nucleotides = ['A', 'C', 'G', 'T']
    
    for i in range(seq_length):
        # Look at the frequency values for A, C, G, T at the current position index 'i'
        max_count = -1
        best_nuc = ''
        for nuc in nucleotides:
            if profile[nuc][i] > max_count:
                max_count = profile[nuc][i]
                best_nuc = nuc
        consensus_list.append(best_nuc)
        
    consensus_string = "".join(consensus_list)
    return consensus_string, profile

if __name__ == "__main__":
    from utils.bioutils import parse_fasta
    
    try:
        current_dir = os.path.dirname(__file__)
        dataset_path = os.path.abspath(os.path.join(current_dir, "..", "Dataset", "rosalind_cons.txt"))
        
        fasta_dict = parse_fasta(dataset_path)
        sequences = list(fasta_dict.values())
        
        consensus, profile_matrix = generate_consensus_and_profile(sequences)
        
        # Print output to match the precise Rosalind layout
        print(consensus)
        for nuc in ['A', 'C', 'G', 'T']:
            counts_str = " ".join(map(str, profile_matrix[nuc]))
            print(f"{nuc}: {counts_str}")
            
    except FileNotFoundError:
        # Fallback minimal sample test case
        sample_seqs = ["ATCCGCTTAG", "AGCGGCTTAG", "ATGCGCTAAG"]
        consensus, profile_matrix = generate_consensus_and_profile(sample_seqs)
        print(consensus)
        for nuc in ['A', 'C', 'G', 'T']:
            print(f"{nuc}: {' '.join(map(str, profile_matrix[nuc]))}")