# PERM -- Enumerating Gene Order

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `combinatorics` `permutations` `itertools`
**Rosalind Link:** https://rosalind.info/problems/perm/
**Date Solved:** 2026-07-05

---

## Biological & Mathematical Background

### Synteny and Gene Order
In genomics, comparing the order of genes across different species helps us understand evolutionary relationships and chromosomal rearrangements. A single chromosome can be thought of as a linear sequence of distinct genes. Over evolutionary time, events like inversions or translocations shuffle these genes around. 

To analyze these rearrangements computationally, we represent a set of n syntenic genes as an ordered list of integers from 1 to n. Finding all possible structural layouts of these genes corresponds to generating all mathematical **permutations** of that set.



### The Factorial Growth
A permutation is an ordering of a set of objects. For a length of n, the total number of unique orderings is given by the factorial function:

n! = n \times (n-1) \times (n-2) \times \dots \times 1

Because factorials grow incredibly fast (e.g., 7! = 5,040, but 11! = 39,916,800), generating permutations requires highly efficient algorithms to prevent running out of system memory. In Python, the standard library provides `itertools.permutations`, which is written in optimized C to yield arrangements with minimal overhead.

---

## Problem Statement

Given a single positive integer n (n \le 7), return:
1. The total number of permutations of length n.
2. A complete list of all these permutations, printed with space-separated integers on individual lines.

---

## Approach

1.  **Generate Target Range:** Create a sequence of integers from 1 to n using `range(1, n + 1)`.
2.  **Compute Permutations:** Invoke Python's native `itertools.permutations()` engine over the sequence. This creates a memory-efficient iterator containing all possible ordered combinations.
3.  **Count Total Sets:** Because we need the total number of arrangements *before* printing them out, we cast the iterator into a concrete list and calculate its length using `len()`, which equates to n!.
4.  **Format and Output:** Print the total count, then loop through the generated tuples, unpacking them into space-separated string outputs.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python Concepts Used
-itertools.permutations: A powerful combinatorial function that generates continuous unique arrangements without repeating any internal elements.

-Argument Unpacking (*perm): The asterisk operator automatically unpacks the native tuple elements (e.g., (1, 2, 3)) directly into individual space-separated arguments inside the print() statement, removing the need for manual string joining.

## Related Problems
-SIGN -- Next step: Enumerating signed permutations to incorporate gene orientation/strand direction (+/-).

-REAR -- Advanced milestone: Calculating the reversal distance required to transform one gene order into another.