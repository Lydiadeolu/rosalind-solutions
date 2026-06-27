# Key decisions: Using str.maketrans() combined with .translate() allows Python 
# to perform character swaps simultaneously across the entire array in highly 
# optimized C under the hood, dodging the bugs that come with manual loop assignments.

import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.bioutils import reverse_complement

if __name__ == "__main__":
    try:
        with open("stronghold/Dataset/rosalind_revc.txt") as file:
            dna_sequence = file.read().strip()
            print(reverse_complement(dna_sequence))
            
    except FileNotFoundError:
        # Fallback textbook test case
        sample = "AAAACCCGGT"
        print(reverse_complement(sample))
