# SUBS -- Finding a Motif in DNA

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `string-searching` `motifs` `sliding-window`
**Rosalind Link:** https://rosalind.info/problems/subs/
**Date Solved:** 2026-06-20

---

## Biological Background

A **genetic motif** is a short, recurring sequence pattern of nucleotides or amino acids that is conjectured to have a biological function. Examples include protein-binding sites (like transcription factors binding to a promoter region), structural signals, or target sites for restriction enzymes. 

Locating these motifs is a key task in identifying regulatory frameworks within organisms. For instance, finding where specific viral sequences integrate into a host genome involves matching short, known structural patterns against massive chromosome strings.

---

## Problem Statement

Given two DNA strings $s$ and $t$ (each of length at most 1 kbp), find all locations where $t$ occurs as a substring of $s$. 

Return the **1-based** starting indices of these positions separated by spaces.

**Example:**
Input: `GATATATGCATATACTTATAT`
Output: `2 4 10`

--- 

## Approach

1. Read the main sequence $s$ and target motif string $t$ from your input dataset file.
2. Calculate the lengths of both strings.Initialize a sliding window of length equal to $|t|$. 
3. Loop from index 0 up to $|s| - |t| + 1$.At each step, extract a slice of $s$ and compare it directly to $t$.If they match, record the loop index plus 1 to satisfy Rosalind's 1-based indexing constraint.
4. Join the resulting integers into a space-separated string array for final output delivery.


## Solution

```Python
# solution.py
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
        with open("C:/Users/adeolu/Downloads/rosalind_subs.txt") as file:
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
``` 
## Key Python Concepts Used

-Sliding Window Slicing (s[i:i+len(t)]): Safely looking at explicit windows inside a sequence array without drifting index markers out-of-bounds.

-map(str, list): A functional utility mapping numerical integers to standard strings quickly so they can be processed by python's " ".join() string concatenator.

## Related Problems
-HAMM -- Prerequisite: fixed parallel string indexing logic.
-PROT -- Next step: translating larger codon frameworks down to specific single-letter sequence outputs.