# DNA -- Counting DNA Nucleotides

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `string-manipulation` `DNA` `counting`
**Rosalind Link:** https://rosalind.info/problems/dna/
**Date Solved:** 2026-06-16

---

## Biological Background

DNA (deoxyribonucleic acid) is a long molecule that contains our unique genetic code. It is composed of four chemical bases (nucleotides): **Adenine (A)**, **Cytosine (C)**, **Guanine (G)**, and **Thymine (T)**. The sequence of these bases determines the biological instructions for building and operating an organism. In bioinformatics, the first step in analyzing a genome is often counting the occurrences of these four nucleotides to understand sequence composition.

---

## Problem Statement

Given a DNA string $s$ (a string of length at most 1000 bp), return four integers separated by spaces, counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in $s$.

---

## Approach

1. Read the DNA sequence string from the input file.
2. Initialize four separate counters (or a dictionary) for A, C, G, and T to zero.
3. Iterate through each character in the string:
   - Increment the corresponding counter based on the character ('A', 'C', 'G', or 'T').
4. Print the values of the counters in the specific order: A, C, G, and T.

---

## Solution

```python
# solution.py
# Key decisions: While one could use string.count(), iterating through the string 
# once is more efficient (O(n) time complexity) for very large sequences. 
# Using a dictionary or the collections.Counter class provides a clean, 
# readable implementation.

def count_nucleotides(dna_string):
    # Initialize counts
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for base in dna_string:
        if base in counts:
            counts[base] += 1
            
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"

if __name__ == "__main__":
    try:
        with open("C:/Users/adeolu/Downloads/rosalind_dna.txt", "r") as file:
            dna_input = file.read().strip()
            print(count_nucleotides(dna_input))
            
    except FileNotFoundError:
        # Fallback test example
        sample_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        print(count_nucleotides(sample_dna))
```

## Key Python Concepts Used
-Dictionaries: Storing the counts of four distinct keys for fast lookup and modification.

-String Iteration: Walking through a string character by character using a for loop.

-File I/O: Reading raw sequence data from a .txt file.


## Related Problems
INI6 -- Prerequisite: Dictionary frequency mapping.

RNA -- Next step: Converting DNA sequences to RNA by substituting T with U.