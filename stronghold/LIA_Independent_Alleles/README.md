# LIA -- Independent Alleles

**Section:** Bioinformatics Stronghold
**Difficulty:** Medium
**Topics:** `probability` `combinatorics` `mendelian-genetics`
**Rosalind Link:** https://rosalind.info/problems/lia/
**Date Solved:** 2026-07-09

---

## Biological & Mathematical Background

### Mendel's Second Law (Independent Assortment)
Mendel's Second Law states that alleles of two or more different genes sort into gametes independently of one another. In this problem, we track an organism that is heterozygous for two separate genes: Aa\ Bb. 

Every generation, an organism mates with a guaranteed Aa\ Bb partner. Regardless of the genotype of the parent chosen from the population pool, because the partner is strictly Aa\ Bb, the probability of *any individual offspring* being a double heterozygote (Aa\ Bb) is **always exactly \frac{1}{4} (0.25)**. 



### The Binomial Probability Framework
At generation k, the total number of organisms in the population grows exponentially to 2^k. Since each offspring's genotype is independent of its siblings, the count of Aa\ Bb organisms follows a **Binomial Distribution**:

* **Number of trials (n):** 2^k (the total population size at generation k).
* **Success probability (p):** 0.25 (the permanent probability of producing an Aa\ Bb offspring).
* **Target (N):** We need to calculate the probability that *at least* N organisms are Aa\ Bb.

Instead of trying to find a single calculation, we sum the Binomial Probability Mass Function (PMF) from N all the way to the maximum population 2^k:

P(X \ge N) = \sum_{x=N}^{2^k} \binom{2^k}{x} \cdot (0.25)^x \cdot (0.75)^{2^k - x}

---

## Problem Statement

Given two positive integers k (k \le 7) and N (N \le 2^k). In each generation, every organism mates with an Aa\ Bb organism to produce exactly two offspring. 

Return the probability that at least N Aa\ Bb organisms will remain in the k-th generation. (Contrapuntally, assume the initial Tom organism at generation 0 is Aa\ Bb). Round the answer to three decimal places.

---

## Approach

1.  **Parse Generations & Boundaries:** Read the integers k and N directly from the file system path using `pathlib`.
2.  **Calculate Total Population (n):** Establish n = 2^k.
3.  **Accumulate Binomial PMF Range:**
    * Loop from x = N up to n.
    * For each step, calculate the combinations using Python's native, optimized `math.comb(n, x)`.
    * Multiply by success weights: 0.25^x \times 0.75^{n-x}.
4.  **Sum and Format:** Add the probabilities together and round the float result to 3 decimal places using `round()`.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python Concepts Used
-math.comb(n, k): Part of Python's standard math library since 3.8. It computes \binom{n}{k} efficiently in internal C structures, preventing overflow or loss of accuracy during multiplication bounds. 

-Exponentiation Operator: Handles float math directly without relying on math.pow(), which provides clean, standard-compliant accuracy layout properties.

---

## Related Problems
-IPRB -- Prerequisite: Calculating simple Mendelian dominant allele probabilities across standard single crosses.
-MEND -- Advanced: Computing full structural genotype probability matrices over complete hierarchical pedigree trees using tree DP algorithms.