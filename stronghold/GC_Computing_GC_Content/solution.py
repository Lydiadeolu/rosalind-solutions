import sys
import os

# Point Python to the root directory for central toolkit imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from utils.bioutils import parse_fasta, calculate_gc_content

def find_highest_gc(fasta_file_path):
    # Parse the file into a dictionary using our utility function
    fasta_dict = parse_fasta(fasta_file_path)
    
    max_id = ""
    max_gc = -1.0
    
    for header, sequence in fasta_dict.items():
        gc_percentage = calculate_gc_content(sequence)
        if gc_percentage > max_gc:
            max_gc = gc_percentage
            max_id = header
            
    return f"{max_id}\n{max_gc:.6f}"

if __name__ == "__main__":
    try:
        print(find_highest_gc("stronghold/Dataset/rosalind_gc.txt"))
    except FileNotFoundError:
        print("Error: 'rosalind_gc.txt' dataset file not found.")
