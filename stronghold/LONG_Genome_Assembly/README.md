# LONG -- Genome Assembly as Shortest Superstring

**Section:** Bioinformatics Stronghold
**Difficulty:** Medium
**Topics:** `genome-assembly` `string-manipulation` `greedy-algorithms`
**Rosalind Link:** https://rosalind.info/problems/long/
**Date Solved:** 2026-06-30

---

## Biological Background

Modern DNA sequencing technologies cannot read whole chromosomes in one piece. Instead, they generate millions of short, randomized fragments called **reads**. The process of piecing these overlapping reads back together to reconstruct the original, long chromosome sequence without a reference map is known as **de novo genome assembly**.

The problem can be modeled computationally as finding the **Shortest Common Superstring (SCS)**. Given a set of strings, we want to construct the shortest possible single string that contains every read in the input set as a substring. This is achieved by finding significant overlaps between the suffixes and prefixes of the reads.

---

## Problem Statement

Given a collection of at most 50 DNA strings of equal length (not exceeding 1 kbp) in FASTA format, return a shortest superstring containing all the given strings. 

The problem guarantees a crucial structural constraint: there exists a unique shortest superstring, and any pair of overlapping strings will overlap by **more than half their length** (\text{overlap} > \frac{\text{len(read)}}{2}).

---

## Approach

Because the problem guarantees that correct overlaps must exceed half the length of the reads, a **Greedy Approximation Algorithm** will reliably find the exact global optimal solution instead of getting trapped in local minima.

1. **FASTA Data Ingestion:** Parse the text dataset file into a flat list of clean DNA sequence strings.
2. **Seed Initialization:** Pop the first sequence out of the pool to act as our initial growing `superstring`.
3. **Greedy Iterative Overlap Search:** Loop through the remaining pool of strings to look for valid prefix or suffix overlaps:
   * **Suffix Overlap:** Check if a read begins with the characters that our `superstring` ends with.
   * **Prefix Overlap:** Check if a read ends with the characters that our `superstring` begins with.
   * Start checking from the maximum possible overlap length down to \lfloor \frac{\text{len(read)}}{2} \rfloor + 1.
4. **String Merging:** As soon as an overlap matching the length constraint is found, merge that read into the master `superstring`, remove it from the pool, and restart the pool scanning cycle.
5. **Termination:** Repeat until the pool is empty and all reads have been assembled into the final superstring.

---

## Solution

See the [Python Solution](solution.py) for this problem.

## Key Python Concepts Used
-Dynamic List Pruning (list.pop()): Modifying the data pool in-place dynamically tracks processed states, ensuring memory overhead decreases down to zero as the algorithm nears completion.

-String Multi-Slicing Window Bounds: Slicing boundaries like read[:-overlap_len] provide an easy way to truncate structural segments before merging them without leaving trailing or duplicated boundaries.

## Related Problems
-GRAPH -- Prerequisite: Modeling sequence overlaps via directed adjacency graphs.
-GREED -- Complementary: Exploring general optimization strategies for greedy heuristics.