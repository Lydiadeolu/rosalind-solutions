# Key decisions: String manipulation in Python is highly efficient. Since strings 
# are immutable, using the built-in .replace() method returns a brand new sequence 
# block in memory instantly, which matches our exact operational requirements.

import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.bioutils import transcribe_dna_to_rna

if __name__ == "__main__":
    try:
        with open("C:/Users/adeolu/Downloads/rosalind_rna.txt") as file:
            dna_sequence = file.read().strip()
            # Call our decoupled utility function
            rna_sequence = transcribe_dna_to_rna(dna_sequence)
            print(rna_sequence)
            
    except FileNotFoundError:
        # Fallback textbook test case
        sample = "GATGGAACTTGACTACGTAAATT"
        print(transcribe_dna_to_rna(sample))
