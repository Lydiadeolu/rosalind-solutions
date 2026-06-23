# Key decisions: Initializing an immutable Bio.Seq object abstracts away manual 
# dictionary lookups. Invoking the .translate() method automatically maps the sequence 
# using the standard genetic code table and cleanly stops execution at termination signals 
# via the to_stop=True flag parameter.

from Bio import SeqIO
from Bio.Seq import Seq

def translate_biopython(rna_sequence: str) -> str:
    """
    Translates RNA to Protein utilizing Biopython's built-in translation mechanics.
    """
    
    rna_obj = Seq(rna_sequence.upper().strip())
    
    # to_stop=True tells Biopython to halt at the first Stop codon and omit it from the string
    protein_obj = rna_obj.translate(to_stop=True)
    
    return str(protein_obj)

if __name__ == "__main__":
    try:
        with open("C:/Users/adeolu/Downloads/rosalind_prot.txt") as file:
            rna_sequence = file.read().strip()
            protein = translate_biopython(rna_sequence)
            print("\n--- Biopython Approach Output ---")
            print(protein)
            
    except FileNotFoundError:
        # Fallback textbook test case
        sample_dna = "GATGGAACTTGACTACGTAAATT"
        print(translate_biopython(sample_dna))
    