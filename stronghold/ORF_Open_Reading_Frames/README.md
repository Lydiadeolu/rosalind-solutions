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

Given a DNA string $s$ of length at most 1 kbp in FASTA format, return every distinct protein string that can be translated from any open reading frame of $s$.

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

```python
# solution.py
# Key decisions: Using Biopython's native .reverse_complement() and .translate() 
# mechanics removes the requirement to manually maintain a 64-entry codon dictionary. 
# Storing valid translations inside a set() structure handles duplicate filtering natively.

import sys
import os 
from Bio.Seq import Seq

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def find_all_orfs(dna_string: str) -> set:
    """
    Scans a DNA string across all 6 reading frames to identify and translate 
    all unique Open Reading Frames.
    """
    dna_seq = Seq(dna_string)
    rev_comp_seq = dna_seq.reverse_complement()
    
    unique_proteins = set()
    
    # Analyze both the forward sequence and its reverse complement
    for reading_strand in [dna_seq, rev_comp_seq]:
        for frame in range(3):
            # Trim the sequence trailing edge to ensure clean triplet division
            trimmed_seq = reading_strand[frame:]
            clean_length = len(trimmed_seq) - (len(trimmed_seq) % 3)
            
            # Translate the entire frame using the standard genetic code (table=1)
            # Stop codons are translated literally as '*' characters
            protein_frame = str(trimmed_seq[:clean_length].translate(table=1))
            
            # Locate all Start ('M') to Stop ('*') coordinate boundaries
            for i, amino_acid in enumerate(protein_frame):
                if amino_acid == 'M':
                    for j in range(i, len(protein_frame)):
                        if protein_frame[j] == '*':
                            # Extract protein segment (excluding the termination asterisk)
                            unique_proteins.add(protein_frame[i:j])
                            break # Halt inner loop at the first stop codon boundary
                            
    return unique_proteins

if __name__ == "__main__":
    from utils.bioutils import parse_fasta
    
    try:
        with open("C:/Users/adeolu/Downloads/rosalind_orf.txt") as file:
        dataset_path = file.read().strip()
        fasta_dict = parse_fasta(dataset_path)
        
        # Pull the primary DNA sequence string from the parsed FASTA dict
        dna_sequence = list(fasta_dict.values())[0]
        
        results = find_all_orfs(dna_sequence)
        for protein in results:
            print(protein)
            
    except FileNotFoundError:
        # Fallback textbook sample test case
        sample_dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACACTGTTGACGGTACTGATCACCATATTGACTCTAATTATTATACATCGTTCCATACAACA"
        for protein in find_all_orfs(sample_dna):
            print(protein)
```

## Key Python Concepts Used
-Sequence Abstraction Layer (Bio.Seq): Utilizing factory methods like .reverse_complement() handles double-stranded mapping logic error-free, while .translate(table=1) eliminates manual dictionary processing.

-Set Matrix Collection (set()): Employing a hashing sequence block to gather output nodes guarantees that overlapping ORFs producing identical physical proteins are deduplicated automatically.

## Related Problems
-PROT -- Prerequisite: Baseline single-frame sequence translation mechanics.
-REVC -- Prerequisite: Constructing stable reverse-complemented structural templates.
-MEND -- Next step: Tracking genomic transmission structures across pedigree nodes.0