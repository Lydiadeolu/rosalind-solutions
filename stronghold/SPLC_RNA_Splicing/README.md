# SPLC -- RNA Splicing

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `string-manipulation` `rna-splicing` `translation`
**Rosalind Link:** https://rosalind.info/problems/splc/
**Date Solved:** 2026-06-26

---

## Biological Background

In eukaryotic cells, newly transcribed pre-mRNA contains interspersed regions that do not code for proteins. Before translation can occur, the sequence must undergo a maturation process called **RNA Splicing**:
* **Introns:** Non-coding genetic segments that must be actively excised from the primary transcript.
* **Exons:** Coding regions that are physically joined together after intron removal to form a continuous, functional mRNA sequence.



If introns are not precisely removed down to the single-nucleotide level, the reading frame shifts during translation, rendering the resulting protein completely non-functional. Once splicing finishes, the mature messenger RNA (mRNA) is ready to be translated by ribosomes into an amino acid sequence.

---

## Problem Statement

Given a DNA string $s$ (of length at most 1 kbp) and a collection of substring introns in FASTA format, return a protein string resulting from splicing all introns from $s$ and executing translation.

---

## Approach

1. **Differentiate Main Sequence vs. Introns:** Parse the incoming multi-entry FASTA file. By convention, the very first sequence entry in the file represents the primary DNA template strand $s$. All subsequent sequence entries represent the isolated target introns.
2. **Exon Concatenation (Intron Stripping):** Iterate through the collection of parsed introns. For each intron sequence, locate its position within the primary strand $s$ and purge it using string slice deletions.
3. **Sequence Translation:** Convert the remaining concatenated exon sequence into its matching amino acid chain. Stop translation when a genetic termination signal (Stop codon) is reached.

---

## Solution

```python
# solution.py
# Key decisions: String manipulation in Python is highly efficient. By iterating through 
# the parsed list of introns and invoking the built-in .replace() method, we excise the non-coding 
# blocks cleanly. Biopython's .translate(to_stop=True) handles the terminal truncation natively.

import sys
import os
from Bio.Seq import Seq

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def splice_and_translate(fasta_file_path: str) -> str:
    """
    Parses a FASTA file containing a main DNA strand followed by introns,
    splices out the introns, and translates the remaining exons into a protein.
    """
    from utils.bioutils import parse_fasta
    
    fasta_dict = parse_fasta(fasta_file_path)
    fasta_keys = list(fasta_dict.keys())
    
    # The first entry is always the primary DNA sequence strand
    primary_dna = fasta_dict[fasta_keys[0]]
    
    # Remaining entries represent the introns to be stripped away
    introns = [fasta_dict[key] for key in fasta_keys[1:]]
    
    # Remove every intron substring from the primary sequence block
    for intron in introns:
        primary_dna = primary_dna.replace(intron, "")
        
    # Cast the mature spliced DNA exon structure into a Bio.Seq object
    exon_seq = Seq(primary_dna)
    
    # Translate directly to protein, truncating output automatically at the first Stop codon
    protein_seq = exon_seq.translate(to_stop=True)
    
    return str(protein_seq)

if __name__ == "__main__":
    try:
        dataset_path = "C:/Users/adeolu/Downloads/rosalind_splc.txt"
        print(splice_and_translate(dataset_path))
        
    except FileNotFoundError:
        # Fallback textbook sample test case
        print("Error: 'rosalind_splc.txt' dataset file not found.")
```

## Key Python Concepts Used
-Ordered FASTA Index Split: Utilizing Python's list(fasta_dict.keys()) handles index positional routing cleanly. This guarantees that the primary template is correctly isolated from the variable-length list of downstream intron arguments.

-Biopython Sequence Compilation (to_stop=True): Utilizing native sequence objects eliminates manual triplet parsing loops, while the to_stop keyword automatically purges terminal characters matching genetic stop parameters.

## Related Problems
-PROT -- Prerequisite: Basic single-frame sequence translation mechanics.
-ORF -- Prerequisite: Managing multiple alternative reading frame coordinates.
-SUBS -- Prerequisite: Locating specific motif substring coordinates inside genomic fields.