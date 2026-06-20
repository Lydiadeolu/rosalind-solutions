# GC -- Computing GC Content

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `string-manipulation` `fasta-parsing` `gc-content`
**Rosalind Link:** https://rosalind.info/problems/gc/
**Date Solved:** 2026-06-20

---

## Biological Background

The **GC-content** of a DNA molecule is the percentage of nitrogenous bases that are either Guanine (G) or Cytosine (C). 

In structural biology, Guanine and Cytosine bind to each other via **three hydrogen bonds**, whereas Adenine and Thymine bind via only **two hydrogen bonds**. Because of this, DNA strands with higher GC-content are more thermo-chemically stable and require higher temperatures to denature (melt apart). 

In genomics, tracking GC-content variations helps identify gene-dense regions, locate promoter sequences, and distinguish between different bacterial species within a mixed environmental sample.

---

## Problem Statement

Given a collection of at most 10 DNA strings in FASTA format (with each string having a length of at most 1000 bp), identify the entry containing the highest GC-content. 

Return the ID of that string, followed by its GC-content percentage formatted to 6 decimal places.

---

## Approach

1. **Manual FASTA Parsing:** Stream the multi-line FASTA file line-by-line. When a line starts with `>`, extract it as a dictionary key. Append subsequent data lines to that key until the next `>` header is encountered.
2. **Calculate Ratios:** Loop through the parsed dictionary entries. For each sequence, compute:
   $$\text{GC}\% = \frac{\text{Count}(G) + \text{Count}(C)}{\text{Total Sequence Length}} \times 100$$
3. **Max Tracking:** Track the maximum value observed along with its corresponding FASTA ID string.
4. **Output Generation:** Output the ID and the calculated value formatted via decimal string precision boundaries.

---

## Solution

```python
# solution.py
# Key decisions: We decouple file parsing and analytical calculation directly 
# to our local utils package. The main execution routine merely handles value tracking 
# state comparisons and string output formatting.

import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.bioutils import parse_fasta, calculate_gc_content

def find_highest_gc(fasta_file_path):
    # Parse the file into a dictionary using our utility function
    fasta_dict = parse_fasta(fasta_file_path)
    
    max_id = ""
    max_gc = -1.0
    
    for header, sequence in fasta_dict.items():
        gc_percentage = calculate_gc_content(sequence)
        if gc_percentage > max_gc:
            max_gc = gc_percentage
            max_id = header
            
    return f"{max_id}\n{max_gc:.6f}"

if __name__ == "__main__":
    try:
        print(find_highest_gc("C:/Users/adeolu/Downloads/rosalind_gc.txt"))
    except FileNotFoundError:
        print("Error: 'rosalind_gc.txt' dataset file not found.")
```

## Key Python Concepts Used
-FASTA Manual Parsing State-Machine: Running an active conditional track loop that groups fragments of sequential strings under structural string key designations dynamically.

-Float Formatting Specification (:.6f): Forcing Python floating-point conversions to render exactly 6 places past the decimal marker to pass strict Rosalind output grading.

## Related Problems
-REVC -- Prerequisite: basic base-pairing properties.

-HAMM -- Next step: evaluating differences between two aligned sequence string values.