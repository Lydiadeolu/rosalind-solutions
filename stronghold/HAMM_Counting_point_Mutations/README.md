# HAMM -- Counting Point Mutations

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `string-comparison` `point-mutations` `hamming-distance`
**Rosalind Link:** https://rosalind.info/problems/hamm/
**Date Solved:** 2026-06-20

---

## Biological Background

An alteration in a genetic sequence is called a **mutation**. The simplest form of mutation is a **point mutation**, which occurs when a single nucleotide base is swapped, deleted, or inserted. When comparing two homologous (evolutionarily related) sequences of equal length, we can quantify the genetic divergence between them by counting the minimum number of single-nucleotide substitutions required to turn one strand into another. 



In computer science and information theory, this count of mismatches between two equal-length strings is known as the **Hamming distance**. It gives geneticists a straightforward baseline metric to estimate evolutionary time distance; the higher the Hamming distance, the longer ago the two sequences shared a common ancestor.

---

## Problem Statement

Given two DNA strings $s$ and $t$ of equal length (not exceeding 1 kbp), return the Hamming distance $d_H(s, t)$.

**Example:**
Input: `GAGCCTACTAACGGGAT`
Output: `CATCGTAATGACGGCCT`

--- 

## Approach

1. Read both sequence lines from the input text file.
2. Ensure both strings are treated as separate variables.
3. Use a counting loop or zipped iterator to compare characters at each index position i
3. Increment a counter every time s[i] \neq t[i].
4. Output the total counter integer.

--- 

## Solution

See the [Python Solution](solution.py) for this problem.

## Key Python Concepts Used

-zip(seq1, seq2): Generates an iterator of tuples where the $i$-th tuple contains the $i$-th element from each of the argument sequences. Perfect for parallel array comparisons.

-Generator Expressions in sum(): Passing a conditional evaluation block like sum(1 for c1, c2 in ...) runs in optimized C loops, avoiding memory overhead from creating explicit intermediary index arrays.

## Related Problems
-GC -- Prerequisite: extracting and manipulating multi-sequence text.
-PROT -- Next step: transcribing and translating sequencing chains into alternative biological character data sets