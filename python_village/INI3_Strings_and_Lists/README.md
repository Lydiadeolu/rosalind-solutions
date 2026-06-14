# INI3 -- Strings and Lists

**Section:** Python Village
**Difficulty:** Easy
**Topics:** `string-manipulation``slicing`
**Rosalind Link:** https://rosalind.info/problems/ini3
**Date Solved:** 2026-06-14

---

## Biological Background

When dealing with genetic code, DNA, RNA, and protein sequences are almost universally represented as text strings. Extracting specific segments from a chromosome—such as isolating a single gene, a promoter region, or a restriction enzyme binding site—fundamentally boils down to string slicing. Knowing exactly how to grab a substring using numerical coordinates is a daily requirement in bioinformatics workflow automation.

---

## Problem Statement

Given a string s (of length at most 10,000 characters) and four integers a, b, c, and d, return two slices of the string:

1. The slice from index a to index b (inclusive).
2. The slice from index c to index d (inclusive).

The output should display these two substrings separated by a single space.

---

## Approach

1. Read the input file to capture the string s on the first line, and the four coordinates on the second   line.
2. Split the coordinate line into four distinct integers: a, b, c, d.
3. Extract the first slice using Python's string slicing protocol syntax: `s[a : b + 1]`. *(Note: Python slicing is exclusive of the stop index, so we add 1 to include character b)*.
4. Extract the second slice using `s[c : d + 1]`.
5. Print both substrings separated by a space.

---

## Solution

```python
# solution.py
# Key decisions: Python strings are 0-indexed. Because Rosalind slice boundaries 
# are inclusive, we adjust the stop index by adding 1 (+1) to match Python's 
# exclusive upper-bound slicing design.

def slice_string_segments(s, a, b, c, d):
    slice1 = s[a : b + 1]
    slice2 = s[c : d + 1]
    return f"{slice1} {slice2}"

if __name__ == "__main__":
    try:
        with open("C:/Users/adeolu/Downloads/rosalind_ini3.txt") as file:
            # Read lines and strip out trailing newline characters
            lines = [line.strip() for line in file.readlines()]
            
            text_string = lines[0]
            # Convert the space-separated numbers on line 2 into integers
            a, b, c, d = map(int, lines[1].split())
            
            print(slice_string_segments(text_string, a, b, c, d))
            
    except FileNotFoundError:
        # Fallback test example from Rosalind description
        sample_str = "HumptyDumptySatOnAWallHumptyDumptyHadAGreatFallAllTheKingsHorsesAndAllTheKingsMenCouldntPutHumptyTogetherAgain"
        print(slice_string_segments(sample_str, 22, 27, 97, 102))

```
## Key Python Concepts Used

-String Slicing (string[start:stop]): Copying a sub-segment of a string. Remember that start is included, but stop is excluded.

-map(int, list): An elegant built-in way to quickly convert a list of split text strings directly into integers all at once.

-f-Strings (Formatted String Literals): Using f"{var1} {var2}" for clean, readable string concatenation.

## Related Problems

INI2 -- Prerequisite: integers and basic assignment.
INI4 -- Next step: control flow and loops.
