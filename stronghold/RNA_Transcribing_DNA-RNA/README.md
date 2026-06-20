# RNA -- Transcribing DNA into RNA

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `string-manipulation` `transcription` `RNA`
**Rosalind Link:** https://rosalind.info/problems/rna/
**Date Solved:** 2026-06-17

---

## Biological Background

In living cells, genetic information flows from DNA to RNA to Protein (a concept known as the Central Dogma of Molecular Biology). **Transcription** is the first major step in this pipeline, where a specific segment of DNA is copied into RNA (specifically messenger RNA, or mRNA) by the enzyme RNA polymerase. 

Chemically, RNA is very similar to DNA, but it possesses two structural differences:
1. It uses a ribose sugar backbone instead of deoxyribose.
2. It replaces the nitrogenous base **Thymine (T)** with **Uracil (U)**. 

During transcription, the structural genetic code sequence remains fundamentally identical in data indexing, except that every instance of `T` is swapped out for a `U`.

---

## Problem Statement

Given a DNA text string $t$ having a length of at most 1000 nucleotides, return its transcribed RNA string (where all occurrences of 'T' are replaced by 'U').

**Example:**
Input: `GATGGAACTTGACTACGTAAATT`
Output: `GAUGGAACUUGACUACGUAAAUU`

---

## Approach

1. Read the input DNA sequence from your Rosalind dataset file.
2. Leverage the project's central toolkit (`utils/bioutils.py`) to systematically parse and transform the sequence data.
3. Use Python's built-in string manipulation properties to convert all instances of the character `'T'` into `'U'`.
4. Output the newly generated RNA sequence string.

---

## Solution

```python
# solution.py
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
        with open("C:/Users/adeolu/Downloads/rosalind_rna.txt", "r") as file:
            dna_sequence = file.read().strip()
            # Call our decoupled utility function
            rna_sequence = transcribe_dna_to_rna(dna_sequence)
            print(rna_sequence)
            
    except FileNotFoundError:
        # Fallback textbook test case
        sample = "GATGGAACTTGACTACGTAAATT"
        print(transcribe_dna_to_rna(sample))
```
## Key Python Concepts Used
-str.replace(old, new): Returns a copy of the target string with all occurrences of substring old replaced by new.

-Decoupled Module Imports: Importing optimized logic from our local utils/bioutils.py file to isolate core computational steps away from structural File I/O interfaces.

## Related Problems
-DNA -- Prerequisite: analyzing raw nucleotide counts.

-REVC -- Next step: generating the reverse complement of a sequence