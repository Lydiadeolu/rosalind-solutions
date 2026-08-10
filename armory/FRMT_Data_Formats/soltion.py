# Key decisions: We process the complete array of target IDs in a single batch call via 
# `Entrez.efetch` to avoid repetitive HTTP handshakes. We then use `SeqIO.parse` over the 
# streamed text buffer to reliably track down the shortest sequence.

import sys
from io import StringIO
from pathlib import Path
from Bio import Entrez, SeqIO

def retrieve_shortest_ncbi_fasta(accession_ids: list[str]) -> str:
    """
    Connects to the NCBI database via Entrez E-utilities, reviews the 
    lengths of all requested IDs, and returns the shortest entry in full FASTA layout.
    """
    # Required by NCBI policy—identifies the application context to API controllers
    Entrez.email = "oyelabiadeolu@gmail.comS"
    
    # Execute batch request to minimize connection handshakes
    try:
        handle = Entrez.efetch(
            db="nucleotide",
            id=",".join(accession_ids),
            rettype="fasta",
            retmode="text"
        )
        fasta_data = handle.read()
        handle.close()
    except Exception as err:
        raise RuntimeError(f"NCBI Efetch request pipeline failed: {err}")

    # Use a StringIO text stream to parse the string data with SeqIO
    records = list(SeqIO.parse(StringIO(fasta_data), "fasta"))
    
    if not records:
        raise ValueError("No valid records were returned from the NCBI server query.")
        
    # Locate the record corresponding to the absolute minimum sequence length
    shortest_record = min(records, key=lambda record: len(record.seq))
    
    # Return the clean, unedited string block configuration
    return shortest_record.format("fasta")

if __name__ == "__main__":
    try:
        # Cross-platform relative file path resolution using Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_frmt.txt"
        
        if dataset_path.exists():
            target_ids = dataset_path.read_text().strip().split()
            if target_ids:
                print(retrieve_shortest_ncbi_fasta(target_ids).strip())
        else:
            raise FileNotFoundError
            
    except FileNotFoundError:
        # Fallback sample tracking case representing typical locus entry profiles
        sample_ids = ["FJ817486", "JX069768", "JX469991"]
        print("Executing Fallback Query on Sample Repository IDs...")
        try:
            print(retrieve_shortest_ncbi_fasta(sample_ids).strip())
        except Exception as api_err:
            print(f"Server connections skipped during local testing bounds: {api_err}")