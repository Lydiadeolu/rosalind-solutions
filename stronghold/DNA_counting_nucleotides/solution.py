# Key decisions: While one could use string.count(), iterating through the string 
# once is more efficient (O(n) time complexity) for very large sequences. 
# Using a dictionary or the collections.Counter class provides a clean, 
# readable implementation.

def count_nucleotides(dna_string):
    # Initialize counts
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for base in dna_string:
        if base in counts:
            counts[base] += 1
            
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"

if __name__ == "__main__":
    try:
        with open("C:/Users/adeolu/Downloads/rosalind_dna.txt", "r") as file:
            dna_input = file.read().strip()
            print(count_nucleotides(dna_input))
            
    except FileNotFoundError:
        # Fallback test example
        sample_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        print(count_nucleotides(sample_dna))
