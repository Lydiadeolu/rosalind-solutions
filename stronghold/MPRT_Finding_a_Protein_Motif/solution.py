# Key decisions: We use the `requests` library to fetch active biological sequences from UniProt.
# We utilize a regex positive lookahead assertion `(?=...)` to intercept overlapping motifs 
# safely, resolving Rosalind's sequence extraction rules perfectly.

import re
import sys
from pathlib import Path
import requests

def fetch_uniprot_sequence(accession_id: str) -> str:
    """
    Queries the UniProt API to download the raw FASTA sequence for a given Accession ID.
    Cleans out potential Markdown link formatting issues introduced during data collection.
    """
    # Fix: If the input ID itself has Markdown formatting like [id](url)
    if "](" in accession_id:
        # Extract just the raw text inside the brackets [A9M5H3]
        accession_id = accession_id.split("]")[0].replace("[", "").strip()

    # Isolate core ID if it contains metadata additions (e.g., PRINTS_HUMAN -> PRINTS)
    core_id = accession_id.split("_")[0].strip()
    
    # Construct a clean URL completely free of bracket artifacts
    url = f"https://rest.uniprot.org/uniprotkb/{core_id}.fasta"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch data for ID: {accession_id} (Status Code: {response.status_code})")
        
    lines = response.text.strip().splitlines()
    sequence = "".join(lines[1:])
    return sequence

def find_motif_positions(sequence: str) -> list[int]:
    """
    Locates 1-based start positions of the N-glycosylation motif N{P}[ST]{P}.
    Utilizes a lookahead window to guarantee overlapping instances are captured.
    """
    # N-glycosylation motif pattern translated into regex lookahead
    # N = Asparagine, [^P] = Not Proline, [ST] = Serine or Threonine
    motif_regex = r"(?=(N[^P][ST][^P]))"
    
    positions = [match.start() + 1 for match in re.finditer(motif_regex, sequence)]
    return positions

if __name__ == "__main__":
    try:
        # Cross-platform relative file path resolution using Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_mprt.txt"
        
        if dataset_path.exists():
            accession_ids = dataset_path.read_text().strip().splitlines()
            
            for entry in accession_ids:
                entry = entry.strip()
                if not entry:
                    continue
                    
                try:
                    protein_seq = fetch_uniprot_sequence(entry)
                    match_indices = find_motif_positions(protein_seq)
                    
                    # Only output entries that actively display matching motifs
                    if match_indices:
                        print(entry)
                        print(" ".join(map(str, match_indices)))
                        
                except Exception as err:
                    print(f"Error processing {entry}: {err}", file=sys.stderr)
        else:
            raise FileNotFoundError
            
    except FileNotFoundError:
        # Fallback textbook sample simulation parameters
        sample_sequence = "MNTTVNYTNPVNSTLI"  # Displays an overlap boundary: NYTN and NSTL
        print("Sample Sequence Analysis Result Indices:", find_motif_positions(sample_sequence))