# Key decisions: Using 'with open()' automatically handles closing files even if 
# an error occurs. We use enumerate(file, 1) to perfectly align Python's 
# standard 0-indexed loop tracking with Rosalind's 1-based even line constraints.

def extract_even_lines(input_path, output_path="output.txt"):
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        # enumerate(..., 1) sets the starting index directly to 1
        for line_num, line in enumerate(infile, 1):
            if line_num % 2 == 0:
                outfile.write(line)

if __name__ == "__main__":
    try:
        extract_even_lines("C:/Users/adeolu/Downloads/rosalind_ini5.txt")
        print("Success! Even lines extracted to 'output.txt'.")
            
    except FileNotFoundError:
        # Fallback inline simulator for testing logic without the external dataset
        import io
        sample_data = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6"
        
        print("--- Fallback Simulated Output ---")
        for num, line in enumerate(io.StringIO(sample_data).readlines(), 1):
            if num % 2 == 0:
                print(line.strip())