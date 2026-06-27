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
        dataset_path = "stronghold/Dataset/rosalind_splc.txt"
        print(splice_and_translate(dataset_path))
        
    except FileNotFoundError:
        # Fallback textbook sample test case
        print("Error: 'rosalind_splc.txt' dataset file not found.")
