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

Given a DNA string s (a string of length at most 1000 bp), return four integers separated by spaces, counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

---

## Approach

1. Read the DNA sequence string from the input file.
2. Initialize four separate counters (or a dictionary) for A, C, G, and T to zero.
3. Iterate through each character in the string:
   - Increment the corresponding counter based on the character ('A', 'C', 'G', or 'T').
4. Print the values of the counters in the specific order: A, C, G, and T.

---

## Solution

See the [Python Solution](solution.py) for this problem.
 
## Key Python Concepts Used
-Dictionaries: Storing the counts of four distinct keys for fast lookup and modification.

-String Iteration: Walking through a string character by character using a for loop.

-File I/O: Reading raw sequence data from a .txt file.


## Related Problems
INI6 -- Prerequisite: Dictionary frequency mapping.

RNA -- Next step: Converting DNA sequences to RNA by substituting T with U.