# PROT -- Translating RNA into Protein

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `translation` `codons` `genetic-code` `strings`
**Rosalind Link:** https://rosalind.info/problems/prot/
**Date Solved:** 2026-06-21

---

## Biological Background



Translation is the final step of the Central Dogma, where cellular machinery (the ribosome) decodes an mRNA sequence to synthesize a specific chain of amino acids, ultimately folding into a functional protein. 

The mRNA sequence is read linearly in non-overlapping triplets called codons. Each codon corresponds to one of 20 standard amino acids used to build proteins. Because there are 4^3 = 64 possible triplet combinations but only 20 amino acids, the genetic code is redundant (multiple codons can code for the same amino acid). Three specific codons function as punctuation markers (Stop codons), signaling the ribosome to halt translation and release the completed protein chain.

---

## Problem Statement

Given an RNA string $s$ corresponding to a strand of mRNA (of length at most 10 kbp), return the protein string encoded by $s$. 

*Note: The translation must terminate immediately upon hitting the first Stop codon.*

**Example:**
Input: `AUGGCCAUGGCGCCCAGAACUGUGAUCAUAUGA`
Output: `MAMAPRTVII`

---

## Manual Approach

1. Read the raw mRNA sequence from the input file.
2. Initialize an empty sequence array to accumulate mapped amino acids.
3. Slice the string into consecutive, non-overlapping chunks of 3 characters (codons).
4. Match each codon against a hardcoded lookup dictionary reflecting the standard RNA Codon Table.
5. If the lookup returns an amino acid letter, append it to the growing protein list.
6. If the lookup encounters a `Stop` codon flag, break out of the processing loop immediately.
7. Merge the accumulated letters into a unified output string.

### 📝 Architectural Note: Manual Implementation vs. Biopython Approach

| Feature | Manual Implementation (`utils/bioutils.py`) | Biopython Approach (`from Bio import ...`) |
| :--- | :--- | :--- |
| **Logic Overhead** | High. Requires hardcoding and maintaining massive static mapping frameworks (like the 64-entry `RNA_CODON_TABLE`). | None. Biological translation maps are handled completely internally by core library configurations. |
| **Edge Cases** | Must be handled manually via nested control flow statements (e.g., checking slice bounds or specifically handling `Stop` flags). | Handled via parameters. Setting `to_stop=True` automatically truncates translation at termination boundaries smoothly. |
| **Alternative Tables**| Tedious. Switching to non-standard codes (like Mitochondrial or Bacterial variants) requires duplicating or updating dictionaries. | Seamless. Allows passing simple integer arguments (e.g., `translate(table=2)`) to swap between NCBI genetic code schemas instantly. |
---

## Solution
#manual approach
See the [Python Solution](solution.py) for this problem.

#biopython approach
See the [Python Solution](prot_Biopython.py) for this problem.
## Key Python Concepts Used

-dict.get(key, default): Safely queries a dictionary without throwing a key error if the data slice is malformed or corrupted.

-Range Step Argument (range(start, stop, step)): Setting the step size to 3 lets us leap directly to the next codon boundary automatically without maintaining manual tracking flag variables.

## Related Problems
-SUBS -- Prerequisite: string slicing loops.

-PRTM -- Next step: using the protein strings generated here to compute real-world molecular weight measurements.