# IPRB -- Mendel's First Law

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `combinatorics` `probability`
**Rosalind Link:** https://rosalind.info/problems/iprb/
**Date Solved:** 2026-06-24

---

## Biological Background

An **allele** is one of two or more alternative forms of a gene that arise by mutation and are found at the same place on a chromosome. For a given trait, organisms inherit one allele from each parent:
* **Homozygous Dominant (XX):** Carries two copies of the dominant allele. Always passes down a dominant allele.
* **Heterozygous (Xx):** Carries one dominant and one recessive allele. Has a 50% chance of passing down either.
* **Homozygous Recessive (xx):** Carries two copies of the recessive allele. Always passes down a recessive allele.

Mendel's First Law (The Law of Segregation) states that allele pairs separate during gamete formation and randomly unite at fertilization. An individual exhibiting the dominant phenotype will be produced if at least one dominant allele (X) is present in its inherited pair (XX or Xx). 

Calculating the probability of dominant offspring within a mixed breeding pool allows geneticists to predict phenotypic distributions across successive generations.

---

## Problem Statement

Given three positive integers k (homozygous dominant), m (heterozygous), and n (homozygous recessive) representing a population containing k + m + n total organisms, return the probability that two randomly selected mating organisms will produce an individual possessing a dominant allele.

Assume any pair of organisms can mate with equal probability, and each couple produces exactly one offspring. The returned float must be formatted to 5 decimal places.

---

## Approach

While we can calculate the probability of getting a dominant allele directly, it is mathematically cleaner to compute the probability of the **complement event** (the probability of producing a homozygous recessive offspring, xx) and subtract it from 1:

\text{P}(\text{Dominant}) = 1 - \text{P}(\text{Recessive})

1. **Total Population Tracking:** Define the population size as T = k + m + n. The total number of unique mating pairs is given by the combination formula \binom{T}{2} = \frac{T(T-1)}{2}.
2. **Isolate Recessive Yields:** There are only three mating combinations capable of producing an offspring with a homozygous recessive (xx) phenotype:
   * **Heterozygous × Heterozygous (m \times m):** Yields a \frac{1}{4} chance of an xx child.
   * **Heterozygous × Homozygous Recessive (m \times n):** Yields a \frac{1}{2} chance of an xx child.
   * **Homozygous Recessive × Homozygous Recessive (n \times n):** Yields a 100\% (1) chance of an xx child.
3. **Probability Derivation:** Sum the targeted pairing combinations multiplied by their biological recessive output weights, divide by total combinations, and subtract from 1.

---

## Solution

See the [Python Solution](solution.py) for this problem.

## Key Python Concepts Used
-Complementary Probability Logic: Using the mathematical identity P(A) = 1 - P(A^c) to optimize code control flow, bypassing the need to map out the more complex branches of dominant allele tracking.

-Float Formatting Specification (:.5f): Enforcing fixed precision rounding limits on floating-point calculations to satisfy the specific structural expectations of the Rosalind checker system.

## Related Problems
-FIB -- Prerequisite: Working with discrete generational intervals.
-MEND -- Next step: Scaled tracking of allele probability matrices across complex structural binary trees.