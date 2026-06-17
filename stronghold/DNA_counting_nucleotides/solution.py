import sys
import os

# Point Python to the root directory for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.bioutils import count_nucleotides

if __name__ == "__main__":
    try:
        with open("rosalind_dna.txt", "r") as file:
            dna = file.read().strip()
            
            # 1. Call your central utility function to get the dict
            counts = count_nucleotides(dna)
            
            # 2. Format the dictionary values into space-separated string for Rosalind
            print(f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}")
            
    except FileNotFoundError:
        # Fallback test case
        sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        counts = count_nucleotides(sample)
        print(f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}")