# PMCH -- Perfect Matchings and RNA Secondary Structures

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `combinatorics` `graphs` `rna-structure` `factorials`
**Rosalind Link:** https://rosalind.info/problems/pmch/
**Date Solved:** 2026-07-08

---

## Biological & Mathematical Background

### RNA Secondary Structure and Graph Matching
Unlike DNA, which forms a stable double helix, single-stranded RNA molecules fold back on themselves to create complex structural shapes known as **secondary structures**. This folding is stabilized by base-pairing bonds between specific nucleotides: Adenine (A) bonds with Uracil (U), and Cytosine (C) bonds with Guanine (G).

We can model an RNA sequence as a graph where the nucleotides are vertices ordered linearly. A **bonding graph** contains edges representing valid potential base pairs. If every single nucleotide in the sequence can find a single matching partner such that no bases are left out, the arrangement forms a **perfect matching** in graph theory.



### The Combinatorial Factorial Calculation
The problem specifies that the RNA string has an equal number of A and U bases, and an equal number of C and G bases. Since A only bonds with U:
* The first A has N_A choices of U to bond with.
* The second A has N_A - 1 choices left, and so on.

This implies that the total number of independent ways to perfectly match all A-U pairs is exactly the factorial of the count of Adenine bases (N_A!). By the fundamental counting principle, because the C-G pairings are completely independent of the A-U pairings, the total number of perfect matchings is the product of both individual factorials:

\text{Total Matchings} = N_A! \times N_C!

---

## Problem Statement

Given an RNA string s of length at most 80 bp in FASTA format, containing an equal number of occurrences of A and U, and an equal number of occurrences of C and G. Return the total possible number of perfect matchings of basepair edges in the bonding graph of s.

---

## Approach

1.  **Parse FASTA Input:** Retrieve the target RNA string using Biopython's `SeqIO` parsing engine managed via cross-platform `pathlib` workflows.
2.  **Count Sub-nucleotides:** Calculate the frequency of Adenine (A) and Cytosine (C) bases using Python's native `.count()` method.
3.  **Compute the Factorial Product:** Calculate N_A! \times N_C! utilizing Python's optimized `math.factorial` library and return the integer total.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python & Biopython Concepts Used
-math.factorial: Standard library module optimized in C that cleanly prevents integer overflow limits when generating massive factorial combinations.

-Bio.SeqIO.read: Ideal for FASTA datasets explicitly containing only one single structural record sequence block, extracting metadata smoothly without tracking generator loops.

---

## Related Problems
-RNA -- Prerequisite: Understanding basic base transcription transitions.

-CAT -- Advanced: Enumerating non-crossing matchings within RNA folding loops using dynamic programming catalogs.