# Key decisions: Using a native Python dict for the codon map provides instantaneous 
# O(1) loop lookups. Slicing with a step parameter of 3 allows straightforward 
# non-overlapping processing of codons.

import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.bioutils import translate_rna_to_protein

if __name__ == "__main__":
    try:
        with open("C:/Users/adeolu/Downloads/rosalind_prot.txt") as file:
            rna_sequence = file.read().strip()
            protein_sequence = translate_rna_to_protein(rna_sequence)
            print(protein_sequence)
            
    except FileNotFoundError:
        # Fallback textbook sample case
        sample = "AUGGCCAUGGCGCCCAGAACUGUGAUCAUAUGA"
        print(translate_rna_to_protein(sample))
