# PRTM -- Calculating Protein Mass

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `mass-spectrometry` `string-manipulation`
**Rosalind Link:** https://rosalind.info/problems/prtm/
**Date Solved:** 2026-06-27

---

## Biological Background

In mass spectrometry, researchers identify and quantify proteins by measuring the mass-to-charge ratio of their constituent peptides. To map these experimental measurements accurately against theoretical protein sequences, bioinformaticians must compute a sequence's **monoisotopic mass**.

* **Monoisotopic Mass:** The total molecular mass computed using the exact mass of the single most abundant, naturally occurring stable isotope for each element (e.g., Carbon-12, Hydrogen-1, Nitrogen-14, Oxygen-16).
* **Average Mass:** Calculated using the average relative atomic weights of elements reflecting natural abundance variations.

Because an amino acid residue is formed by a peptide bond reaction that eliminates a water molecule (H_2O), the monoisotopic mass of a protein is computed by summing the individual monoisotopic masses of its standard amino acid residues and then adding the mass of a single water molecule to account for the terminal groups.

---

## Problem Statement

Given a protein string P of length at most 1000 aa, return the total monoisotopic mass of P.

The constant monoisotopic masses of the 20 standard amino acid residues are predefined via the standard monoisotopic mass table. The final calculated mass must be returned as a float formatted to 3 decimal places.

---

## Approach

1. **Incorporate Monoisotopic Constant Weights:** Embed the 20 standard amino acid residue mass values directly into a local static lookup table (dictionary).
2. **Linear Sequence Translation Mapping:** Scan the incoming protein string character-by-character. Look up each individual amino acid residue in the dictionary and accumulate its monoisotopic mass into a running total tracking float variable.
3. **Incorporate Terminal Water Correction:** Add the monoisotopic mass of a standard water molecule (H_2O \approx 18.01056\text{ Da}) to the final accumulated sum to restore the terminal groups.
4. **Precision Output Rounding:** Format the final floating-point value to exactly 3 decimal places to ensure synchronization with the Rosalind grading checker.

\text{Total Mass} = \left( \sum_{i=1}^{|P|} \text{Mass}(P[i]) \right) + \text{Mass}(H_2O)

---

## Solution

See the [Python Solution](solution.py) for this problem.

## Key Python Concepts Used
-Dictionary Pointer Map Exploration: Using hash-map lookups allows the sequence scan loop to parse through long structural strings without hitting performance bottleneck matrices.

-Generator Expressions in Vectorized Arithmetic (sum()): Passing an inline generator block directly to sum() calculates total sequence mass values on-the-fly without the overhead of creating or keeping intermediate lists in system memory.

## Related Problems
-PROT -- Prerequisite: Translating RNA codon segments into protein strings.
-SPLC -- Prerequisite: Splicing genetic structures prior to terminal translation routing.
-SPEC -- Next step: Inferring a protein sequence by processing sequential weight deltas derived from a mass spectrum matrix.