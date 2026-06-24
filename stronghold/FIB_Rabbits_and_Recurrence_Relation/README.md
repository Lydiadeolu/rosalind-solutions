# FIB -- Rabbits and Recurrence Relation

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `combinatorics` `dynamic-programming` `recurrence-relations`
**Rosalind Link:** https://rosalind.info/problems/fib/
**Date Solved:** 2026-06-24

---

## Biological Background

In 1202, Leonardo of Pisa (Fibonacci) introduced an idealized mathematical model tracking the reproductive patterns of rabbit populations. This framework serves as a foundational baseline for tracking structural population dynamics, generation cycles, and ecological metrics.

In this model, we track breeding pairs over generations under the following biological assumptions:
1. **Maturation Lag:** Rabbit pairs require exactly one month to mature from juveniles into reproductive adults.
2. **Survival Parameter:** Once mature, rabbit pairs remain fertile and survive indefinitely (this variant enforces a zero-mortality environment with no death cycles).
3. **Litter Yield (k):** Every mature, reproductive pair produces a fixed batch of k new juvenile pairs each month.

---

## Problem Statement

Given positive integers n \le 40 (months) and k \le 5 (litter size), return the total number of rabbit pairs that will be present after n months.

Return the final integer tracking the absolute volume of breeding pairs remaining in the system at the conclusion of the generational cycle.

---

## Approach

1. **Identify Preceding State Influx:** A recurrence relation defines an ongoing mathematical sequence where each individual term acts as a function of its preceding elements.
2. **Calculate Ratios:** To track populations without exponential computing overhead, calculate each generation using a modified Fibonacci recurrence formula:
   F_n = F_{n-1} + k \cdot F_{n-2}
3. **Apply Boundary Conditions:** Initialize structural tracking states utilizing the base constraints F_1 = 1 (initial juvenile pair) and F_2 = 1 (initial pair reaches maturity).
4. **Bottom-Up Dynamic Programming:** Run a linear loop from month 3 up to month n, shifting previous generation values forward in memory using an iterative array technique to bypass deep call stack exhaustion.

---

## Solution

```python
# solution.py
# Key decisions: Python handles arbitrarily large scalar integers automatically, meaning
# we don't have to worry about numerical integer overflow as the sequence scales.
# Using a simple iterative swap loop optimizes space complexity down to O(1) memory.


def solve_fib(n: int, k: int) -> int:
    """
    Computes the total rabbit pairs after n months with litter size k.
    """
    # Handle baseline boundary cases
    if n == 1 or n == 2:
        return 1
        
    # Set up sliding variables for bottom-up dynamic programming
    parent_generation = 1  # F_1
    current_generation = 1 # F_2
    
    for _ in range(3, n + 1):
        # Next term = Adults alive from previous month + (Fertile grandparents * litter yield)
        next_generation = current_generation + (parent_generation * k)
        
        # Slide state values forward in the execution cycle
        parent_generation = current_generation
        current_generation = next_generation
        
    return current_generation

if __name__ == "__main__":
    try:
        with open("C:/Users/adeolu/Downloads/rosalind_fib.txt") as file:
            # Read lines and strip out trailing newline spacing markers
            n, k = map(int, file.read().strip().split())
            print(solve_fib(n, k))
            
    except FileNotFoundError:
        # Fallback textbook sample test case
        print(solve_fib(5, 3))
```

## Key Python Concepts Used
-Bottom-Up Iterative State-Machine: Running a manual, controlled tracking loop that shifts generational metrics forward sequentially in memory using dynamic variable swapping instead of slow, deep recursive functions.

-Biopython Omission Analysis: While sequence transformations (FASTA) are routed through Biopython modules, pure mathematical modeling algorithms and combinatorial matrix loops are kept as Manual Implementations to guarantee absolute execution speed and eliminate external library overhead.

## Related Problems
-DNA -- Prerequisite: baseline scalar logic inputs.
-FIBD -- Next step: expanding the recurrence relation model to incorporate structural rabbit mortality rates (death cycles).