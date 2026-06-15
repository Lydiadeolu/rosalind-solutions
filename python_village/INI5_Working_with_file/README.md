# INI5 -- Working with files

**Section:** Python village
**Difficulty:** Easy
**Topics:** `file-io` `line-parsing`
** Rosalind link:** https://rosalind.info/problems/ini5/
**Dte Solved:** 2026-06-15

---

## Biological Background

Real-world biological datasets—such as multi-gigabyte FASTQ sequencing reads, structural PDB files, or downstream variant calling files (VCFs)—are structured line-by-line as plain text. Programmers rarely load these files entirely into computer memory at once because it causes crashes. Instead, streaming files line-by-line allows scripts to scan, filter, and extract critical properties (like isolating header rows vs. raw genetic sequence rows) highly efficiently.

---

## Problem Statement

Given a text file containing at most 1000 lines, return a new file containing all the **even-numbered lines** from the original file. 

*Note: The problem uses a 1-based indexing system for human readability (i.e., you need to extract the 2nd line, 4th line, 6th line, etc.).*

---

## Approach

1. Open the source input file for reading.
2. Initialize a line counter tracking variable at `1` (or use Python's built-in `enumerate()` starting at index `1`).
3. Iterate through the file line by line to maintain memory efficiency.
4. Use the modulo operator (`%`) to evaluate if the current line number is even (`line_number % 2 == 0`).
5. If it evaluates to true, print or write that line.
6. Cleanly close the target file streams.

---

## Solution

```python
# solution.py
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
        extract_even_lines("C:/Users/adeolu/Downloads/rosalind_ini5.txt" "r")
        print("Success! Even lines extracted to 'output.txt'.")
            
    except FileNotFoundError:
        # Fallback inline simulator for testing logic without the external dataset
        import io
        sample_data = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6"
        
        print("--- Fallback Simulated Output ---")
        for num, line in enumerate(io.StringIO(sample_data).readlines(), 1):
            if num % 2 == 0:
                print(line.strip())
```

## Key Python Concepts Used
-Context Managers (with open()): The safest, most modern structural approach to file handling in Python. It automatically deals with file system stream cleanups.

-Enumerate(iterable, start): Generates a running count tracking sequence alongside individual elements during a loop, removing the need for manual counter additions (i += 1).

-File Modes ('r' vs 'w'): Specifying read privileges vs destructive write/overwrite access when initializing a file connection.

## Related Problems
INI4 -- Prerequisite: conditionals and looping logic.

INI6 -- Next step: key-value storage structures.