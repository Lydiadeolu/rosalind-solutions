# SIGN -- Orienting Random Orderings

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `combinatorics` `permutations` `backtracking` `genomic-rearrangements`
**Rosalind Link:** https://rosalind.info/problems/sign/
**Date Solved:** 2026-07-15

---

## Biological & Mathematical Background

### Signed Permutations and Genome Rearrangements
During evolution, chromosomes can undergo large-scale mutations where a segment of DNA is cut, flipped, and reinserted back into the genome. This process is called a **chromosome reversal** (or inversion). 

Because DNA has a clear orientation (5' to 3' polarity), a flipped segment changes both its relative order and its directional orientation on the strand. In bioinformatics, we model this by assigning a **positive or negative sign** to each gene sequence.

A **signed permutation** of length n is an ordering of the numbers \{1, 2, \dots, n\} where each element is additionally assigned either a positive (+) or a negative (-) sign.

<Image src="image_agent_tag_5852864895816585384" alt="Black and white textbook scan demonstrating cycle notation and permuted group index maps in permutation group mathematics" caption="Mathematical Foundation of Permutation Groups" />

### How Many Signed Permutations Exist?
To calculate the total number of unique signed permutations of length n:
1. There are standardly n! ways to arrange the absolute values of the integers \{1, 2, \dots, n\}.
2. For each unique arrangement, each of the n positions can independently be either positive (+) or negative (-), yielding 2^n unique sign configurations.

By the fundamental counting principle, the total number of signed permutations of length n is:

T(n) = 2^n \times n!

For n = 3, this yields:

2^3 \times 3! = 8 \times 6 = 48 \text{ unique signed permutations}

---

## Problem Statement

Given a positive integer n \le 6.

Return the total number of signed permutations of length n, followed by a complete list of all such signed permutations (each on a separate line). The order of the permutations does not matter.

---

## Approach

An elegant way to solve this in Python is to separate the combinatorial concerns into two distinct standard library operations:
1.  **Generate base orderings:** Use `itertools.permutations` to get all n! layouts of the absolute numbers \{1, 2, \dots, n\}.
2.  **Generate sign distributions:** Use `itertools.product` with values `[1, -1]` repeated n times to generate all 2^n sign orientation matrices.
3.  **Combine states:** For every permutation, multiply each element by its corresponding sign vector index and print the result.

---

## Solution


---


---

## Related Problems
PERM -- Prerequisite: Generating standard unsigned permutations of length n.
REGC -- Advanced: Calculating genomic distance using signed reversal permutation trees.