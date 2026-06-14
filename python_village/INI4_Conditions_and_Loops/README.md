# INI4 -- Conditions and Loops

**Section:** Python Village
**Difficulty:** Easy
**Topics:** `loops` `conditionals` `math`
**Rosalind Link:** https://rosalind.info/problems/ini4/
**Date Solved:** 2026-06-14

---

## Biological Background

Bioinformatics datasets are massive, often containing millions of sequences, base pairs, or genomic coordinates. To extract meaningful information, computational biologists write scripts that iterate over ranges of positions (using loops) and isolate specific regions based on strict criteria—such as checking if a nucleotide sequence matches a target motif or if an expression value falls outside a normal threshold (using conditional statements).

---

## Problem Statement

Given two positive integers a and b (a < b), return the sum of all odd integers from a through b, inclusively.

For example, if a = 10 and b = 15, the odd integers in that range are 11, 13, and 15. Their sum is 11 + 13 + 15 = 39.

---

## Approach

1. Read the input values for a and b from the dataset file.
2. Initialize a running sum tracker to `0`.
3. Use a loop to iterate through all numbers starting from a up to and including b. 
   - *Note: In Python's `range(start, stop)`, the `stop` value is exclusive, so we must loop until `b + 1`.*
4. For each number in the loop, use the modulo operator (`%`) to check if the number is odd (`number % 2 != 0`).
5. If the number is odd, add it to the running sum tracker.
6. Print the total sum.

---

## Solution

```python
# solution.py
# Key decisions: Using a loop with a conditional check is clear and instructive. 
# While this can also be solved using mathematical series formulas or step-wise 
# ranges (e.g., range(start, b+1, 2)), a standard loop explicitly fulfills 
# the problem's goal of practicing conditions and loops.

def sum_odds_in_range(a, b):
    total_sum = 0
    # b + 1 ensures that 'b' is included in our iteration range
    for num in range(a, b + 1):
        if num % 2 != 0:  # Check if the number is odd
            total_sum += num
    return total_sum

if __name__ == "__main__":
    try:
        with open("C:/Users/adeolu/Downloads/rosalind_ini4.txt") as file:
            # Parse the two space-separated integers
            a, b = map(int, file.read().strip().split())
            print(sum_odds_in_range(a, b))
            
    except FileNotFoundError:
        # Fallback test example from Rosalind description
        print(sum_odds_in_range(100, 200))
```

## Key python Concepts Used
-for Loops and range(): Iterating through a sequence of numbers. range(a, b + 1) generates values from a to b.

-Modulo Operator (%): Returns the remainder of a division. Any integer n where n % 2 != 0 is mathematically odd.

-Conditional if statement: Executing specific block code logic only when a given boolean expression evaluate to True.

## Related Problems

INI3 -- Prerequisite: string and slicing basics

INI5 -- Next step: reading and manipulating text files line by lineS