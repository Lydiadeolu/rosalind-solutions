# LGIS -- Longest Increasing Subsequence

**Section:** Bioinformatics Stronghold
**Difficulty:** Medium
**Topics:** `dynamic-programming` `binary-search` `permutations`
**Rosalind Link:** https://rosalind.info/problems/lgis/
**Date Solved:** 2026-07-07

---

## Biological & Mathematical Background

### Gene Order and Subsequences
During evolutionary divergence, large-scale genomic mutations can scramble the order of genes along a chromosome. When comparing the genomes of two related species, we can map corresponding genes to a permutation of integers. Identifying the **Longest Increasing Subsequence (LIS)** and the **Longest Decreasing Subsequence (LDS)** allows bioinformaticians to calculate the minimum number of evolutionary inversion operations required to align the two genomes.



### Algorithmic Optimization: Patience Sorting
A naive dynamic programming solution to find the LIS takes O(n^2) time, which becomes dangerously slow as the permutation length approaches n = 10,000. 

To handle long genetic permutations efficiently, we implement an O(n \log n) approach known algorithmically as **Patience Sorting** (or the Patience Game):
1. **Piles Elements:** We iterate through the permutation, maintaining an array of the smallest tail elements of all increasing subsequences found so far.
2. **Binary Search Insertion:** For each new number, we use binary search (`bisect`) to find its structural position in our active sequence piles, updating the sequence mapping seamlessly.
3. **Backtracking:** By storing tracking pointers to parent elements, we reconstruct the exact sequence path back to the origin.

---

## Problem Statement

Given a positive integer n (n \le 10,000) and a permutation \pi of length n, return:
1. A longest increasing subsequence of \pi.
2. A longest decreasing subsequence of \pi.

The elements of each subsequence should be separated by spaces.

---

## Approach

1.  **Parse Permutation Input:** Read the sequence of numbers safely using `pathlib` parsing patterns.
2.  **Isolate the LIS (O(n \log n)):**
    * Maintain a tracking array `tails` where `tails[i]` stores the smallest tail value of an increasing subsequence of length `i+1`.
    * Use Python's built-in `bisect.bisect_left` to binary search the correct insertion index for each incoming value.
    * Use a parent pointer tracking array to reconstruct the full sequence path.
3.  **Isolate the LDS:** Finding the longest decreasing subsequence on a sequence X is mathematically identical to finding the longest *increasing* subsequence on the inverted complement values of X. We can invert the array logic or negate values to reuse the exact same core LIS engine.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python Concepts Used
-bisect.bisect_left: Part of Python's standard library. It finds insertion points in sorted arrays using an optimized O(\log n) binary division algorithm.

-Path Transformation (-x inversion): An elegant mathematical trick that cuts our required codebase in half by modifying our input data structure instead of writing a completely separate descending search logic branch.

---

## Related Problems
PERM -- Prerequisite: Working with complete, un-shuffled genomic permutation matrices.

REAR -- Advanced: Computing the minimum reversal distance boundaries between random gene sets.