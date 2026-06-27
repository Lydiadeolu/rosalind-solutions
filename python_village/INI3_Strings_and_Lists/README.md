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

See the [Python Solution](solution.py) for this problem.

---

## Key Python Concepts Used

-String Slicing (string[start:stop]): Copying a sub-segment of a string. Remember that start is included, but stop is excluded.

-map(int, list): An elegant built-in way to quickly convert a list of split text strings directly into integers all at once.

-f-Strings (Formatted String Literals): Using f"{var1} {var2}" for clean, readable string concatenation.

---

## Related Problems

INI2 -- Prerequisite: integers and basic assignment.
INI4 -- Next step: control flow and loops.
