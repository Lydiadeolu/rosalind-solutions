# INI6 -- Dictionaries

**Section:** Python Village
**Difficulty:** Easy
**Topics:** `dictionaries` `word-counts` `hash-maps`
**Rosalind Link:** https://rosalind.info/problems/ini6/
**Date Solved:** 2026-06-15

---

## Biological Background

Counting the frequency of specific words is a fundamental operation in bioinformatics, heavily utilized in **k-mer counting** (identifying short, overlapping substrings of DNA). Tracking k-mers allows researchers to find regulatory motifs, calculate genomic signatures for species identification, and assemble fragmented sequencing reads into a complete genome. Using an efficient data structure to store these counts ensures that scripts run quickly even when dealing with millions of sequences.

---

## Problem Statement

Given a string $s$ of words separated by spaces (up to 10,000 characters), return the frequency of each word in the string. The output should list each word followed by its count, with each word-count pair printed on a new line. The order of the output lines does not matter.

---

## Approach

1. Read the text string from the input file.
2. Split the string into individual words using spaces as delimiters.
3. Initialize an empty dictionary (hash map) to track the words and their respective counts.
4. Loop through the list of words:
   - If the word is already a key in the dictionary, increment its value by 1.
   - If it is not present, add it to the dictionary with an initial value of 1.
5. Iterate through the dictionary items and print each key-value pair separated by a space.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python Concepts Used

-Dictionaries (dict): Hash-table based structures storing data as key: value pairs.

-string.split(): Breaks text into a list of words, automatically handling variable whitespace and newlines when called without arguments.

-dict.items(): A loop utility method that returns viewable tuples of both the (key, value) pairs simultaneously.

---

## Related Problems
INI5 -- Prerequisite: processing string inputs and file lines.

# Next track step: 

 migrating this exact dictionary counting logic to map biological nucleotide frequencies.