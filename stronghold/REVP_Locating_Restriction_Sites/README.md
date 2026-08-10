# REVP -- Locating Restriction Sites

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `string-algorithms` `molecular-biology` `reverse-complement`
**Rosalind Link:** https://rosalind.info/problems/revp/
**Date Solved:** 2026-07-11

---

## Biological & Mathematical Background

### Restriction Enzymes and Reverse Palindromes
Restriction enzymes are specialized molecular scissors produced by bacteria to defend against viral invaders. These enzymes slice through foreign DNA molecules at highly specific sequence boundaries called **restriction sites**. 

Unlike a standard linguistic palindrome (e.g., "radar"), a DNA restriction site forms a **reverse palindrome**. This means that the sequence read forward from 5' to 3' on the coding strand is completely identical to the sequence read forward from 5' to 3' on the complementary non-coding strand. 

For example, the string `GAATTC` is a perfect reverse palindrome:
* Coding strand: `5'-GAATTC-3'`
* Complementary strand: `3'-CTTAAG-5'` \rightarrow Reversing it yields `5'-GAATTC-3'`

<Image src="image_agent_tag_18089837806874106721" alt="Vector diagram illustrating a circular plasmid map highlighting core structural features such as a promoter, origin of replication, and specific positions marked as restriction sites where restriction enzymes cut open the sequence topology" caption="Plasmid Topology and Restriction Sites" />

---

## Problem Statement

Given a DNA string s of length at most 1 kbp in FASTA format. Return the 1-based start positions and lengths of every reverse palindrome in s that has a length between 4 and 12 base pairs (inclusive).

The output formatting rules mandate that each valid entry occupies a standalone line displaying: `[Start Position] [Subsequence Length]`.

---

## Approach

1.  **Parse FASTA Dataset:** Extract the raw DNA text using Biopython's `SeqIO.read` combined with a `pathlib` workspace tracking map.
2.  **Generate a Complement Table:** Use Python's built-in `str.maketrans` utility to perform fast nucleotide mapping dictionary swaps (A \leftrightarrow T and C \leftrightarrow G).
3.  **Sliding Window Scanning Matrix:**
    * Iterate through every starting index position i from 0 up to the string length boundary.
    * For each starting index, try window lengths L ranging sequentially from 4 up to 12.
    * Extract the substring slice, calculate its reverse complement, and flag it if both sequences match exactly.

---

## Solution


---

## Key Python & Biopython Concepts Used
-str.translate(str.maketrans(...)): Executes character array manipulation entirely inside underlying optimized C-buffers. This approach is much cleaner than compiling custom dictionary evaluation loops.

-[::-1] Slicing Syntax: Reverses an existing string template natively via memory stride parameters, avoiding manual element recursion stacks.

---

## Related Problems
-REVC -- Prerequisite: Basic generation of standard reverse complement sequences.

-ORF -- Advanced: Scanning reading frames for initiation codons using reverse complement strands.