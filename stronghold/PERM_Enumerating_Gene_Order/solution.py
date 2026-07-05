import sys
from pathlib import Path
from itertools import permutations

def generate_gene_orders(n: int) -> list:
    """
    Generates all unique permutations of length n.
    """
    elements = range(1, n + 1)
    return list(permutations(elements))

if __name__ == "__main__":
    try:
        # Cross-platform relative workspace file loading via Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_perm.txt"
        
        if dataset_path.exists():
            n_genes = int(dataset_path.read_text().strip())
        else:
            raise FileNotFoundError
            
        all_permutations = generate_gene_orders(n_genes)
        
        # 1. Build the output content string in memory
        output_lines = [str(len(all_permutations))]
        for perm in all_permutations:
            output_lines.append(" ".join(map(str, perm)))
            
        output_content = "\n".join(output_lines)
        
        # 2. Define the output path in the Dataset directory and export the file
        output_path = dataset_path.parent / "rosalind_perm_output.txt"
        output_path.write_text(output_content)
        
        # Also print to console so you can verify it immediately
        print(output_content)
        print(f"\n[Success] Output exported cleanly to: {output_path.resolve()}")
            
    except FileNotFoundError:
        # Fallback textbook sample test case simulation (n = 3)
        sample_perms = generate_gene_orders(3)
        print(len(sample_perms))
        for perm in sample_perms:
            print(*(perm))