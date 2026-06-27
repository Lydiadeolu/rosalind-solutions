# Key decisions: Python's native string slicing s[i:i+n] operates extremely fast. 
# While regex could be used, an explicit sliding window is clean, avoids library 
# overhead, and handles overlapping cases out of the box.

import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.bioutils import find_motif_indices

if __name__ == "__main__":
    try:
        with open("stronghold/Dataset/rosalind_subs.txt") as file:
            lines = [line.strip() for line in file if line.strip()]
            
            if len(lines) >= 2:
                s = lines[0]
                t = lines[1]
                
                indices = find_motif_indices(s, t)

                # Convert integer list to space-separated string array
                print(" ".join(map(str, indices)))
            else:
                print("Error: Dataset file must contain at least two lines.")
                
    except FileNotFoundError:
        # Fallback textbook sample case
        s_sample = "GATATATGCATATACTT"
        t_sample = "ATAT"
        indices = find_motif_indices(s_sample, t_sample)
        print(" ".join(map(str, indices)))