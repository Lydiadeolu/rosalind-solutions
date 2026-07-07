# LCSM -- Finding a Shared Motif

**Section:** Bioinformatics Stronghold
**Difficulty:** Medium
**Topics:** `string-algorithms` `suffix-arrays` `longest-common-substring` `dynamic-programming`
**Rosalind Link:** https://rosalind.info/problems/lcsm/
**Date Solved:** 2026-07-07

---

## Biological & Mathematical Background

### Identifying Shared Motifs
In comparative genomics, identifying identical genetic subsystems shared across highly divergent organisms helps pinpoint crucial structural genes or regulatory regions conserved by evolutionary selection. Mathematically, given a collection of structural DNA sequences, our goal is to isolate the **Longest Common Substring (LCS)** that appears natively within *every single* sequence in the pool.



### Algorithmic Strategy: Binary Search + Suffix Structures
While basic Dynamic Programming (DP) works flawlessly for finding the LCS of *two* strings in O(|S_1| \cdot |S_2|) time, expanding a standard DP grid to accommodate k separate sequences requires a tensor space matrix growing at O(N^k), which causes immediate memory collapse when handling large datasets.

To achieve production-grade performance, we leverage a hybrid algorithmic strategy:
1. **Binary Search on Substring Length:** The minimum possible length of an LCS is `0`, and the maximum possible length is the length of the shortest string in our dataset (M). We can binary search across this range [0, M].
2. **Rolling Suffix Window Verification:** For a target length L, we extract all candidate substrings of length L from the shortest sequence and verify whether they exist across all other sequences using fast substring checks or a **Generalized Suffix Array/Tree**. This reduces the computational complexity to O(N \cdot K \log M).

---

## Problem Statement

Given a collection of k (k \le 100) DNA strings in FASTA format, where each string possesses a length of at most 1 kbp. Return a longest common substring of the collection. (If multiple solutions exist, you may return any one).

---

## Approach

1.  **Parse Input Sequences:** Use Biopython's `SeqIO` engine to read the downloaded FASTA file via canonical `pathlib` workflows.
2.  **Isolate Shortest Boundary:** Identify the shortest sequence in the dataset. The maximum possible common motif cannot exceed the length of this string.
3.  **Binary Search Window Framework:**
    * Establish boundaries `low = 1` and `high = len(shortest_string)`.
    * Take the midpoint `mid = (low + high) // 2`.
    * Check if any substring of length `mid` from our shortest string is uniformly present in all other sequences.
    * If a valid common motif is discovered, update our best result and shift our search upward (`low = mid + 1`). Otherwise, tighten the evaluation ceiling (`high = mid - 1`).

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python & Biopython Concepts Used
-Bio.SeqIO.parse: Streamlines parsing complex multi-line FASTA records into clean pythonic objects without manual string cleaning loops.

-all() Generator Expression: Evaluates short-circuit logical boolean tracking across data matrices. all(candidate in seq for seq...) will stop searching the moment a single sequence fails the alignment match, preserving memory runtime.

---

## Related Problems
SUBS -- Prerequisite: Locating simple, non-generalized sub-motifs inside a target sequence template.

LONG -- Advanced: Overlapping matching suffix-prefix boundaries to completely assemble full-length master genomes.