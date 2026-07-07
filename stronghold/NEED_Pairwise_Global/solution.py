# Key decisions: We implement `Bio.Align.PairwiseAligner` as recommended in modern 
# Biopython documentation. We route paths robustly using `pathlib.Path`.

import sys
from pathlib import Path
from Bio import Entrez
from Bio import Align
from Bio import SeqIO

# Identify yourself to NCBI
Entrez.email = "your_email@example.com"

def fetch_sequences(accession_ids: list) -> list:
    """
    Fetches raw FASTA sequence strings from GenBank using remote Entrez E-fetch.
    """
    id_query = ",".join(accession_ids)
    with Entrez.efetch(db="nucleotide", id=id_query, rettype="fasta", retmode="text") as handle:
        records = list(SeqIO.parse(handle, "fasta"))
    return [str(record.seq) for record in records]

def compute_global_alignment_score(seq1: str, seq2: str) -> int:
    """
    Initializes a global pairwise alignment matrix using custom structural penalties.
    """
    aligner = Align.PairwiseAligner()
    aligner.mode = 'global'
    
    # Inject problem parameters
    aligner.match_score = 5
    aligner.mismatch_score = -4
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -1
    
    # Compute and return the optimal score
    score = aligner.score(seq1, seq2)
    return int(score)

if __name__ == "__main__":
    try:
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_need.txt"
        
        if dataset_path.exists():
            accessions = dataset_path.read_text().strip().split()
        else:
            raise FileNotFoundError
            
        sequences = fetch_sequences(accessions)
        alignment_score = compute_global_alignment_score(sequences[0], sequences[1])
        print(alignment_score)
        
    except FileNotFoundError:
        # Fallback textbook sample test case simulation
        # (Using minimal matching sequences to verify aligner configuration)
        s1 = "ATCA"
        s2 = "ATCA"
        print(compute_global_alignment_score(s1, s2))