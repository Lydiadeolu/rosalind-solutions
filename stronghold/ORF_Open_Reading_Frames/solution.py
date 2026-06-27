# Key decisions: Using Biopython's native .reverse_complement() and .translate() 
# mechanics removes the requirement to manually maintain a 64-entry codon dictionary. 
# Storing valid translations inside a set() structure handles duplicate filtering natively.

import sys
import os 
from Bio.Seq import Seq

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def find_all_orfs(dna_string: str) -> set:
    """
    Scans a DNA string across all 6 reading frames to identify and translate 
    all unique Open Reading Frames.
    """
    dna_seq = Seq(dna_string)
    rev_comp_seq = dna_seq.reverse_complement()
    
    unique_proteins = set()
    
    # Analyze both the forward sequence and its reverse complement
    for reading_strand in [dna_seq, rev_comp_seq]:
        for frame in range(3):
            # Trim the sequence trailing edge to ensure clean triplet division
            trimmed_seq = reading_strand[frame:]
            clean_length = len(trimmed_seq) - (len(trimmed_seq) % 3)
            
            # Translate the entire frame using the standard genetic code (table=1)
            # Stop codons are translated literally as '*' characters
            protein_frame = str(trimmed_seq[:clean_length].translate(table=1))
            
            # Locate all Start ('M') to Stop ('*') coordinate boundaries
            for i, amino_acid in enumerate(protein_frame):
                if amino_acid == 'M':
                    for j in range(i, len(protein_frame)):
                        if protein_frame[j] == '*':
                            # Extract protein segment (excluding the termination asterisk)
                            unique_proteins.add(protein_frame[i:j])
                            break # Halt inner loop at the first stop codon boundary
                            
    return unique_proteins

if __name__ == "__main__":
    from utils.bioutils import parse_fasta
    
    try:
            current_dir = os.path.dirname(__file__)
            dataset_path = os.path.abspath(os.path.join(current_dir, "..", "Dataset", "rosalind_orf.txt"))
            fasta_dict = parse_fasta(dataset_path)
        
            # Pull the primary DNA sequence string from the parsed FASTA dict
            dna_sequence = list(fasta_dict.values())[0]
        
            results = find_all_orfs(dna_sequence)
            for protein in results:
                print(protein)
            
    except FileNotFoundError:
        # Fallback textbook sample test case
        sample_dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACACTGTTGACGGTACTGATCACCATATTGACTCTAATTATTATACATCGTTCCATACAACA"
        for protein in find_all_orfs(sample_dna):
            print("Error: The specified file path was not found, using sample DNA")
            print(protein)
