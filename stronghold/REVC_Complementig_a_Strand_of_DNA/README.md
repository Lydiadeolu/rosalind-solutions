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

See the [Python Solution](solution.py) for this problem.

## Key Python Concepts Used
-str.maketrans() and str.translate(): An efficient pair of internal functions designed to replace multiple single characters at the same time without interfering step-overlaps.

-Extended Slicing Syntax ([::-1]): A standard, elegant Python paradigm used to reverse sequences or strings efficiently via index skipping steps.

## Related Problems
-RNA -- Prerequisite: basic string modification.

-GC -- Next step: calculating the proportional fraction of G and C nucleotides within structural FASTA records.