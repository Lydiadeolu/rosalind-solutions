# REVC -- Complementing a Strand of DNA

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `string-manipulation` `reverse-complement` `DNA`
**Rosalind Link:** https://rosalind.info/problems/revc/
**Date Solved:** 2026-06-18

---

## Biological Background

DNA exists natively as a double-stranded helix. The two strands run in opposite directions (**antiparallel**), meaning one strand runs from the 5' end to the 3' end, while its partner runs from 3' to 5'. The strands are held together by complementary base pairing rules discovered by Erwin Chargaff:

- **Adenine (A)** pairs exclusively with **Thymine (T)**
- **Cytosine (C)** pairs exclusively with **Guanine (G)**

When molecular biologists read sequence data from secondary storage, it is conventionally written from the 5' to 3' direction. Therefore, to discover the structure of the opposite strand, you must not only swap every single base with its complement, but you must also **reverse** the entire string so that the output remains structurally compliant with the 5' to 3' orientation standard.

---

## Problem Statement

Given a DNA text string $s$ of length at most 1000 bp, return the reverse complement string of $s$.

**Example:**
Input: `AAAACCCGGT`
Output: `ACCGGGTTTT`

---

## Approach

1. Read the input sequence $s$ from the file.
2. Initialize a baseline mapping table where characters `A, T, C, G` translate directly to `T, A, G, C`.
3. Complement the string using the mapping table.
4. Reverse the resulting string to ensure proper 5' to 3' sequencing layout constraints.
5. Save or print the final reverse-complemented string.

---

## Solution

```python
# solution.py
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
        with open("C:/Users/adeolu/Downloads/rosalind_revc.txt") as file:
            dna_sequence = file.read().strip()
            print(reverse_complement(dna_sequence))
            
    except FileNotFoundError:
        # Fallback textbook test case
        sample = "AAAACCCGGT"
        print(reverse_complement(sample))
```

## Key Python Concepts Used
-str.maketrans() and str.translate(): An efficient pair of internal functions designed to replace multiple single characters at the same time without interfering step-overlaps.

-Extended Slicing Syntax ([::-1]): A standard, elegant Python paradigm used to reverse sequences or strings efficiently via index skipping steps.

## Related Problems
-RNA -- Prerequisite: basic string modification.

-GC -- Next step: calculating the proportional fraction of G and C nucleotides within structural FASTA records.