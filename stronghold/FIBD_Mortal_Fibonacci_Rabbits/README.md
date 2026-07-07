# FIBD -- Mortal Fibonacci Rabbits

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `dynamic-programming` `combinatorics` `sliding-window`
**Rosalind Link:** https://rosalind.info/problems/fibd/
**Date Solved:** 2026-07-05

---

## Biological & Mathematical Background

### The Lifespan Constraint
In the classic Fibonacci model, rabbits are immortal, growing infinitely at an exponential rate. The **Mortal Fibonacci Rabbits** problem introduces biological realism by enforcing a strict **lifespan constraint (m)**. Once a pair of rabbits reaches m-months of age, they die.

Instead of tracking a single total population integer, we must track the exact population distributed by age bracket across time.



### Dynamic Programming with a Sliding Window
Using a primitive recursive function (F_n = F_{n-1} + F_{n-2}) fails here because we need memory of what happened exactly m months ago to account for deaths. 

To solve this efficiently in O(n) time and O(m) space, we track age cohorts using a **sliding window array** (or a double-ended queue, `collections.deque`). 
* The index of the array represents the **age of the rabbit pairs** in months (from 0 to m-1).
* Each month, the population shifts down the pipeline like a conveyor belt.

---

## Problem Statement

Given two integers:
* n: The total number of months to simulate.
* m: The lifespan of a rabbit pair in months.

Return the total number of rabbit pairs that remain alive at the n-th month, assuming that a single pair is born in month 1 and rabbits begin reproducing upon reaching 2 months of age.

---

## Approach

1.  **Initialize the Cohort Window:** Create a list or `deque` of size m initialized to zeros. At month 1, place our initial newborn pair at index `0` (representing age "0 months old").
2.  **Time-Step Simulation:** Loop from month 2 up to month n. For each step:
    * **Calculate New Births:** Every pair aged 1 month or older reproduces. Thus, the number of new births is the sum of all elements from index `1` to `m-1`.
    * **Shift Age Cohorts:** Shift the entire population right by 1 month. The rabbits at index `m-1` have reached their maximum lifespan and are dropped from the array (representing death).
    * **Introduce Newborns:** Place the calculated birth total into index `0`.
3.  **Aggregate Survivors:** At the conclusion of the loop, return the sum of all remaining values across the entire window.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python Concepts Used
-Sliding Window Slicing ([newborns] + age_cohorts[:-1]): Elegantly manages the generation translation by shifting all items right while simultaneously appending the new generation to the front and truncating the deceased tail.

-pathlib.Path File Resolution: Safely routes input files without hardcoded strings or OS slash errors.

---

## Related Problems
FIB -- Prerequisite: Tracking exponential rabbit populations without a lifespan ceiling.

RABB -- Next step: Managing advanced dynamic generation modeling algorithms.