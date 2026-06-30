# CONS -- Consensus and Profile

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `string-manipulation` `matrix-manipulation` `genomics`
**Rosalind Link:** https://rosalind.info/problems/cons/
**Date Solved:** 2026-06-30

---

## Biological Background

When multiple structural DNA sequences exhibit functional similarities across different organisms, they are often aligned together to identify conserved regions. This collection of aligned sequences can be represented quantitatively by a **Profile Matrix** and qualitatively by a **Consensus Sequence**.

* **Profile Matrix ($P$):** A $4 \times n$ matrix (where $4$ represents the four DNA nucleotides A, C, G, T, and $n$ is the length of the genetic strands). Each cell $P_{i,j}$ stores the exact frequency count of nucleotide $i$ at position $j$ across all aligned strands.
* **Consensus Sequence:** A singular representative DNA sequence constructed by selecting the most frequent nucleotide occurring at each sequential column index of the profile matrix.



---

## Problem Statement

Given a collection of at most 15 DNA strings of equal length (at most 1 kbp each) presented in FASTA format, return:
1. A consensus string matching the matrix parameters.
2. The complete profile matrix formatted as four rows showing individual nucleotide count frequencies sorted in the alphabetical order: `A`, `C`, `G`, `T`.

---

## Approach

1. **Multi-Line FASTA Ingestion:** Parse the input text file to load all raw DNA sequences into an array of uniform-length strings.
2. **Matrix Initialization:** Detect the exact length $n$ of the DNA strands. Construct a nested profile structure tracking counts for `A`, `C`, `G`, and `T` at each index from $0$ to $n-1$.
3. **Column Column Sweeps:** Iterate index-by-index across the horizontal sequence length. For every string in the collection, increment the count of the character observed at that position.
4. **Max-Frequency Consensus Extraction:** Loop vertically through the completed matrix columns. At each index, find the nucleotide that holds the maximum frequency value and append it to the growing consensus sequence string.
5. **Standard Output Formatting:** Print the consensus sequence followed by the formatted rows of the profile matrix to match the space-separated text layout expected by Rosalind.

---

## Solution

See the [Python Solution](solution.py) for this problem.

## Key Python Concepts Used
-Array Pre-allocation: Using [0] * seq_length instantiates arrays with accurate size footprints instantly, avoiding the performance overhead of continuous .append() operations during frequency calculation loops.

-map() Vector Type Casting: Utilizing map(str, array) efficiently converts integers into printable string blocks, allowing " ".join() to execute quickly without explicit item-by-item parsing loops.

## Related Problems
-DNA -- Prerequisite: Basic single-strand nucleotide frequency counts.
-GC -- Prerequisite: Processing sequence arrays stored inside FASTA containers.
-HAMM -- Complementary: Evaluating basic mismatches between single pairs instead of complete matrices.