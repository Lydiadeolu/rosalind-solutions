# Key decisions: Wrapping the raw text in an immutable Biopython Seq object promotes 
# the string to a validated biological entity. Invoking the native .transcribe() 
# method executes optimized C-level manipulations under the hood, ensuring type safety 
# and structural scalability without manual string replacement overhead.

from Bio import SeqIO
from Bio.Seq import Seq

def transcribe_biopython(dna_sequence: str) -> str:
    """
    Transcribes DNA to RNA utilizing Biopython's dedicated Seq object.
    """
    # 1. Cast the raw string into an immutable Biopython Seq object
    dna_obj = Seq(dna_sequence.upper())
    
    # 2. Invoke the built-in biological transcription method
    rna_obj = dna_obj.transcribe()
    
    # 3. Convert back to string for Rosalind text submission output
    return str(rna_obj) 

if __name__ == "__main__":
    try:
        with open("stronghold/Dataset/rosalind_rna.txt") as file:
            dna_sequence = file.read().strip()
            rna_sequence = transcribe_biopython(dna_sequence)
            print("\n--- Biopython Approach Output ---")
            print(rna_sequence)
    except FileNotFoundError:
        # Fallback textbook test case
        sample_dna = "GATGGAACTTGACTACGTAAATT"
        print(transcribe_biopython(sample_dna))
    