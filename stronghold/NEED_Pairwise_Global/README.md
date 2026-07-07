# NEED -- Pairwise Global Alignment

**Section:** Bioinformatics Armory
**Difficulty:** Easy
**Topics:** `biopython` `sequence-alignment` `dynamic-programming`
**Rosalind Link:** https://rosalind.info/problems/need/
**Date Solved:** 2026-07-03

---

## Biological Background

### Global vs. Local Alignment
Sequence alignment is the foundational mechanism used to identify structural homology and evolutionary divergence between biomolecules:
* **Global Alignment:** Driven by the **Needleman-Wunsch algorithm**, this technique forces an alignment spanning the entire length of both target sequences. It is optimized for sequences of highly similar length distributions.
* **Local Alignment:** Driven by the **Smith-Waterman algorithm**, this framework isolates highly conserved local domains or sub-fragments within sequences that are otherwise structurally divergent.

### Scoring Dynamics & Penalties
Alignments are scored using statistical metrics that mirror natural evolutionary pressures:
1.  **Substitution Matrices:** Define the weight of structural mutations. In protein spaces, empirical matrices like `BLOSUM62` track mutation likelihoods based on physical properties.
2.  **Affine Gap Penalties:** Modeled via structural penalties divided into **Gap Opening** (heavy penalty for initiating a deletion/insertion sequence) and **Gap Extension** (minor penalty for extending a gap that has already been introduced).

---

## Problem Statement

Given two GenBank Accession IDs, retrieve their raw DNA sequences from NCBI and compute the maximum global alignment score using the following parameters:
* **Match Reward:** 5
* **Mismatch Penalty:** -4
* **Gap Open Penalty:** -10
* **Gap Extend Penalty:** -1

---

## Approach

1.  **Remote Data Ingestion:** Use `Bio.Entrez.efetch` to programmatically retrieve the complete sequence data matching the target Accession IDs directly from the NCBI `nucleotide` database in FASTA format.
2.  **Engine Instantiation:** Initialize `Bio.Align.PairwiseAligner` (the modern successor to the legacy `Bio.pairwise2` module).
3.  **Parameter Injection:** Configure the aligner object mode to `global` and map the exact numerical scoring constraints into its execution grid.
4.  **Score Calculation:** Execute the aligner over both downloaded sequences and pull the maximum alignment score.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python & Biopython Concepts Used
-Bio.Align.PairwiseAligner: The industry-standard Biopython module for computing sequence distances via optimized C backends.

-Pathlib Architecture: Utilizing Path(__file__).resolve() avoids clumsy string handling, creating cross-platform file manipulation structures cleanly.

---

## Related Problems
-GBK -- Prerequisite: Understanding basic remote connections to NCBI's Entrez gateway.

-EDTA -- Stronghold equivalent: Writing the dynamic programming alignment matrix completely from scratch.