# ORF -- Open Reading Frames

**Section:** Bioinformatics Stronghold
**Difficulty:** Medium
**Topics:** `string-manipulation` `translation` `open-reading-frames`
**Rosalind Link:** https://rosalind.info/problems/orf/
**Date Solved:** 2026-06-25

---

## Biological Background

An **Open Reading Frame (ORF)** is a structural portion of a DNA sequence that has the potential to be translated into a protein. An ORF begins with a specific **Start Codon** (`ATG` in DNA, `AUG` in RNA), followed by a continuous string of triplet codons, and ends abruptly at a **Stop Codon** (`TAA`, `TAG`, or `TGA`).

Because DNA is double-stranded and directional, any given DNA sequence contains **six possible reading frames**:
* **Forward Frames (+1, +2, +3):** Read 5' to 3' on the sense strand starting at offset positions 0, 1, and 2.
* **Reverse Frames (-1, -2, -3):** Read 5' to 3' on the opposite antisense strand (the reverse complement) starting at offset positions 0, 1, and 2.



In computational genomics, identifying candidate ORFs across all six possible configurations is the fundamental first step toward ab initio gene prediction and protein annotation.

---

## Problem Statement

Given a DNA string s of length at most 1 kbp in FASTA format, return every distinct protein string that can be translated from any open reading frame of s.

The output strings can be returned in any order, but the collection must contain no duplicate values.

---

## Approach

1. **Compute Reverse Complement:** Generate the reverse complement of the incoming DNA sequence to capture frames -1, -2, and -3.
2. **Scan Six Reading Frames:** For both the forward and reverse complement sequences, iterate through the three base offset positions (0, 1, and 2).
3. **Isolate Codon Triplets:** Group the sequence at the current offset into non-overlapping groups of 3 characters. 
4. **Identify Translation Coordinates:** Scan each frame for a Start codon (`ATG`). Once found, track subsequent codons until a Stop codon (`TAA`/`TAG`/`TGA`) is encountered. Translate that precise window into its matching amino acid chain.
5. **Deduplicate Candidates:** Store all translated protein candidates inside a Python `set` structure to automatically eliminate redundant sequences produced by overlapping frames.

---

## Solution

See the [Python Solution](solution.py) for this problem.

## Key Python Concepts Used
-Sequence Abstraction Layer (Bio.Seq): Utilizing factory methods like .reverse_complement() handles double-stranded mapping logic error-free, while .translate(table=1) eliminates manual dictionary processing.

-Set Matrix Collection (set()): Employing a hashing sequence block to gather output nodes guarantees that overlapping ORFs producing identical physical proteins are deduplicated automatically.

## Related Problems
-PROT -- Prerequisite: Baseline single-frame sequence translation mechanics.
-REVC -- Prerequisite: Constructing stable reverse-complemented structural templates.
-MEND -- Next step: Tracking genomic transmission structures across pedigree nodes.