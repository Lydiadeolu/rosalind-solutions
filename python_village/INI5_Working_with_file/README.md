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

See the [Python Solution](solution.py) for this problem.

---

## Key Python Concepts Used
-Context Managers (with open()): The safest, most modern structural approach to file handling in Python. It automatically deals with file system stream cleanups.

-Enumerate(iterable, start): Generates a running count tracking sequence alongside individual elements during a loop, removing the need for manual counter additions (i += 1).

-File Modes ('r' vs 'w'): Specifying read privileges vs destructive write/overwrite access when initializing a file connection.

---

## Related Problems
INI4 -- Prerequisite: conditionals and looping logic.

INI6 -- Next step: key-value storage structures.