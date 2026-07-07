# Key decisions: Rather than manually looping over the sequence characters, 
# we wrap the raw text input inside Biopython's native `Seq` object and 
# execute its highly-optimized C-underpinned `.count()` method.

import sys
import os
from Bio.Seq import Seq

def count_nucleotides_with_biopython(dna_string: str) -> tuple:
    """
    Wraps a string in a Biopython Seq object to compute nucleotide base frequencies.
    """
    # Instantiating the biological sequence object wrapper
    dna_seq = Seq(dna_string)
    
    # Executing native optimized counter methods
    a_count = dna_seq.count("A")
    c_count = dna_seq.count("C")
    g_count = dna_seq.count("G")
    t_count = dna_seq.count("T")
    
    return a_count, c_count, g_count, t_count

if __name__ == "__main__":
    try:
        # Dynamically locate the dataset folder using relative workspace routing
        current_dir = os.path.dirname(__file__)
        dataset_path = os.path.abspath(os.path.join(current_dir, "..", "Dataset", "rosalind_ini.txt"))
        
        with open(dataset_path, "r") as file:
            dna_payload = file.read().strip()
            
        counts = count_nucleotides_with_biopython(dna_payload)
        print(f"{counts[0]} {counts[1]} {counts[2]} {counts[3]}")
            
    except FileNotFoundError:
        # Fallback textbook sample test case
        sample_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGT"
        counts = count_nucleotides_with_biopython(sample_dna)
        print(f"{counts[0]} {counts[1]} {counts[2]} {counts[3]}")