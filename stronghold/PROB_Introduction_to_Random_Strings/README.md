# PROB -- Introduction to Random Strings

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `probability` `string-algorithms` `math` `logarithms`
**Rosalind Link:** https://rosalind.info/problems/prob/
**Date Solved:** 2026-07-09

---

## Biological & Mathematical Background

### Random Strings and GC-Content
The **GC-content** of a DNA string is the percentage of its bases that are either Guanine (G) or Cytosine (C). When modeling DNA sequences randomly, we assume that the bases G and C are equally likely to appear, and A and T are equally likely to appear. 

Therefore, given a specific GC-content value x:
* The probability of choosing either G or C is \frac{x}{2}.
* The probability of choosing either A or T is \frac{1 - x}{2}.

### Preventing Float Underflow via Log-Probabilities
If we want to calculate the total probability of an entire DNA sequence matching a specific random composition model, we would normally multiply the individual probability weights of each base together. However, because probabilities are numbers between 0 and 1, multiplying them repeatedly for long strings causes the value to shrink exponentially toward 0. This quickly triggers a **floating-point underflow error**, where the computer loses accuracy and rounds the number down to a hard `0.0`.

To completely bypass this hardware limitation, we apply the algebraic laws of logarithms. Instead of multiplying raw probabilities, we add their logarithms together:

\log_{10}(P(s)) = \sum_{i=1}^{|s|} \log_{10}(P(s[i]))

This transforms microscopic decimal products into stable, easily manageable negative sums.

---

## Problem Statement

Given a DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1. 

Return an array B of the same length as A, where B[i] represents the common logarithm (\log_{10}) of the probability that a random string constructed with the GC-content A[i] will match s exactly. Round each output number to three decimal places.

---

## Approach

1.  **Parse String and Array Inputs:** Read the DNA string template s and float array values safely using `pathlib` splitting patterns.
2.  **Iterate Across GC-Content Benchmarks:** For every independent GC-content float entry x in array A:
    * Establish the baseline component log-weights:
        * `log_gc = math.log10(x / 2.0)`
        * `log_at = math.log10((1.0 - x) / 2.0)`
    * Step through each character in the string s. Add `log_gc` to the total if the base is G or C, and add `log_at` if the base is A or T.
3.  **Format Solution:** Collect the compiled logarithmic sums, round each to 3 decimal places using `round()`, and join them as space-separated tokens.

---

## Solution
See the [Python Solution](solution.py) for this problem.


---

## Key Python Concepts Used
-math.log10(x): Computes base-10 logarithms natively in efficient C. Utilizing this instead of standard multiplying algorithms keeps execution stable regardless of input length boundaries.

-in Tuple Memberships: Checking base in ("G", "C") runs inside an immutable lookup space, keeping sequential loops fast and legible.

---

## Related Problems
-DNA -- Prerequisite: Basic counting of individual nucleotide weights.

-RSTR -- Advanced: Finding the exact probability that at least one matching random string is generated among multiple independent production sequences.