# Key decisions: Using Python's built-in zip() iterator allows us to stream 
# through both sequence arrays simultaneously without manually managing index 
# integer boundaries, resulting in highly clean, pythonic code.

import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.bioutils import hamming_distance

if __name__ == "__main__":
    try:
        with open("stronghold/Dataset/rosalind_hamm.txt") as file:
            # Read lines and strip out trailing newline spacing markers
            lines = [line.strip() for line in file if line.strip()]
            
            if len(lines) >= 2:
                s = lines[0]
                t = lines[1]
                print(hamming_distance(s, t))
            else:
                print("Error: Dataset does not contain two lines.")
                
    except FileNotFoundError:
        # Fallback sample textbook test case
        s_sample = "GAGCCTACTAACGGGAT"
        t_sample = "CATCGTAATGACGGCCT"
        print(hamming_distance(s_sample, t_sample)) 