# GRAPH -- Overlap Graphs

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `graph-theory` `string-manipulation` `genome-assembly`
**Rosalind Link:** https://rosalind.info/problems/graph/
**Date Solved:** 2026-06-30

---

## Biological Background

In modern high-throughput DNA sequencing, machines cannot read whole chromosomes at once. Instead, they break the genome into millions of short fragments called **reads**. To reconstruct the original genome, bioinformaticians construct an **Overlap Graph** (specifically a directed graph layout) to model how these reads fit back together.

* **Vertices (Nodes):** Represent the individual sequenced reads.
* **Directed Edges:** A directed arrow connects vertex s to vertex t (s \rightarrow t) if the suffix (ending sequence) of read s matches the prefix (beginning sequence) of read t.

This overlap mapping serves as the foundational framework for **de novo genome assembly** using Overlap-Layout-Consensus (OLC) pipelines.

---

## Problem Statement

Given a collection of DNA strings in FASTA format (at most 100 strings, each of length at most 10 kbp), return the adjacency list of the overlap graph O_3. 

An edge exists from string s to string t if and only if:
1. The suffix of length 3 of s matches the prefix of length 3 of t (\text{Suffix}_3(s) = \text{Prefix}_3(t)).
2. s \neq t (no self-loops are allowed).

Each line of the output must represent an edge as a space-separated pair of FASTA identifiers: `ID_s ID_t`.

---

## Approach

1. **FASTA Data Parsing:** Read the input file using the repository's central toolkit to extract a dictionary containing FASTA IDs as keys and their corresponding DNA strings as values.
2. **Matrix Permutation Mapping:** Use an all-pairs nested loop structure (O(N^2) complexity) to evaluate every possible sequence node combination against every other sequence node.
3. **Overlapping Boundary Check:**
   * For the source node (s), extract the last 3 characters: `s_string[-3:]`.
   * For the target node (t), extract the first 3 characters: `t_string[:3]`.
4. **Self-Loop Suppression:** Explicitly check that `id_s != id_t` before matching to ensure a sequence does not accidentally map to itself.
5. **Adjacency Output Formatting:** Whenever a match is confirmed, print the source FASTA ID followed by the destination FASTA ID separated by a single space character.

---

## Solution

See the [Python Solution](solution.py) for this problem.

## Key Python Concepts Used
String Negative Slicing (seq[-3:]): Using negative indices provides an explicit, clean way to pull trailing characters from the end of a string regardless of its overall variable length.

Permutation Evaluation vs Combination: Because directed graphs care about direction (s \rightarrow t is fundamentally different from t \rightarrow s), evaluating pairs across nested loops tracks asymmetric routing paths perfectly.

## Related Problems
-RECOMB -- Next step: Constructing de Bruijn graphs using k-mer counts for advanced sequence assembly
-SUBS -- Prerequisite: Locating specific string coordinates via standard substring scanners.
-AMM -- Related: Measuring exact string mismatches instead of edge overlaps.