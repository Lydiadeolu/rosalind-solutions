# IEV -- Calculating Expected Offspring

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `probability` `statistics` `mendelian-genetics`
**Rosalind Link:** https://rosalind.info/problems/iev/
**Date Solved:** 2026-07-15

---

## Biological & Mathematical Background

### Mendelian Inheritance & Dominant Phenotypes
In simple Mendelian genetics, organisms inherit one allele from each parent to form their genotype. If an allele is **dominant** (represented as uppercase, e.g., A), an offspring needs only one copy (AA or Aa) to display the dominant physical trait (phenotype). If both inherited alleles are **recessive** (aa), they display the recessive phenotype.

<Image src="image_agent_tag_826214058090696584" alt="Diagram showing a genetic test cross with Punnett squares demonstrating how heterozygous and homozygous dominant parents yield different ratios of dominant to recessive offspring" caption="Mendelian Monohybrid Cross Outcomes" />

### Expected Value
In probability, the **expected value** E[X] of a random variable is the weighted average of all possible outcomes. 

If we assume every breeding pair produces exactly **two offspring**, we can calculate the expected number of dominant offspring by determining the dominant-trait probability for each parental mating configuration.

| Genotype Pairing | Probability of Dominant Offspring | Expected Offspring displaying Dominant Phenotype (per 2 offspring) |
|---|---|---|
| **1. AA \times AA** | 1.0 (100\%) | 2 \times 1.0 = 2.0 |
| **2. AA \times Aa** | 1.0 (100\%) | 2 \times 1.0 = 2.0 |
| **3. AA \times aa** | 1.0 (100\%) | 2 \times 1.0 = 2.0 |
| **4. Aa \times Aa** | 0.75 (75\%) | 2 \times 0.75 = 1.5 |
| **5. Aa \times aa** | 0.50 (50\%) | 2 \times 0.50 = 1.0 |
| **6. aa \times aa** | 0.0 (0\%) | 2 \times 0.0 = 0.0 |

By linearity of expectation, the total expected number of dominant-phenotype offspring is the sum of the expectations across all pairings:

E[X] = 2(x_1) + 2(x_2) + 2(x_3) + 1.5(x_4) + 1.0(x_5) + 0(x_6)

Where x_n is the count of parental pairs of type n.

---

## Problem Statement

Given six non-negative integers corresponding to the number of couples in a population possessing each of the six genotype pairings listed above (in order).

Return the expected number of offspring displaying the dominant phenotype in the next generation, assuming that every couple has exactly two offspring.

---

## Approach

Because this problem is mathematically straightforward, we do not need complex simulations or recursive functions.
1. Ingest the 6 space-separated integers representing the couple counts.
2. Store the expected dominant offspring constants for each couple type: `[2.0, 2.0, 2.0, 1.5, 1.0, 0.0]`.
3. Calculate the dot product (pairwise multiplication and sum) of the couples list and the constants list.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Performance & Optimization

This solution runs in \mathcal{O}(1) time complexity and uses \mathcal{O}(1) space complexity because the array size is permanently fixed at 6 elements. It can process populations containing millions of couples instantly.

---

## Related Problems
-IPRB -- Prerequisite: Calculating mendelian dominant-trait probability for a single random pair draw.
-MEND -- Advanced: Computing genotype probability distributions over complex structural pedigree trees using dynamic programming.