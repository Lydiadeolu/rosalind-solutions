# MULT -- Multiple Alignment

**Section:** Bioinformatics Stronghold
**Difficulty:** Hard
**Topics:** `dynamic-programming` `string-algorithms` `multiple-alignment` `hyperlattice-backtracking`
**Rosalind Link:** https://rosalind.info/problems/mult/
**Date Solved:** 2026-07-15

---

## Biological & Mathematical Background

### Generalizing Pairwise Alignment to 4 Dimensions
In pairwise sequence alignment, we use a 2D dynamic programming grid where we transition through 3 directions (match/mismatch, gap in sequence 1, or gap in sequence 2). To align $k$ sequences simultaneously, we must generalize this to a **$k$-dimensional hyperlattice**. 

For $k = 4$ DNA sequences, we construct a **4D Dynamic Programming Tensor** of size:

$$(L_1 + 1) \times (L_2 + 1) \times (L_3 + 1) \times (L_4 + 1)$$

Where $L_i$ represents the length of the $i$-th sequence.

### Transition Vectors (Neighborhood States)
In a 4D grid, the number of incoming directions to any cell $(i, j, k, l)$ is $2^k - 1$. For 4 sequences, there are exactly $2^4 - 1 = 15$ possible transition movements. Each vector represents whether we consume a character from sequence $n$ (denoted as $-1$ or $1$ step backward) or insert a gap symbol `-` (denoted as $0$ steps backward):

$$\Delta \in \{0, -1\}^4 \setminus \{(0,0,0,0)\}$$

### Scoring Function: Sum-of-Pairs (SP)
The score of any aligned column in multiple alignment is obtained by taking the sum of scores over all possible $\binom{k}{2}$ unique pairs of symbols in that column:

*   **Match (including matched gaps `-` and `-`):** $0$ points
*   **Mismatch (any mismatch or gap-character pair):** $-1$ points

For 4 sequences, there are $\binom{4}{2} = 6$ pairs to evaluate for every column.

$$\text{Score}(\text{Column}) = \sum_{1 \le a < b \le 4} \text{PairScore}(S_a[\text{col}], S_b[\text{col}])$$

---

## Problem Statement

Given a collection of four DNA strings of length at most 10 bp in FASTA format.

Return the maximum multiple alignment score, followed by a multiple alignment of the four strings achieving this maximum.

---

## DP Recurrence Relation

For a coordinate vector $\mathbf{v} = (i,j,k,l)$, the optimal score $S(\mathbf{v})$ is calculated as:

$$S(\mathbf{v}) = \max_{\mathbf{\Delta} \in \mathcal{D}} \Big\{ S(\mathbf{v} + \mathbf{\Delta}) + \text{Sum-Of-Pairs}(\mathbf{v}, \mathbf{\Delta}) \Big\}$$

Where $\mathcal{D}$ is the set of 15 directional offset vectors, and $\text{Sum-Of-Pairs}(\mathbf{v}, \mathbf{\Delta})$ extracts the characters from the active sequences matching the indices consumed by $\mathbf{\Delta}$ (assigning `-` to any index left unconsumed by a $0$ offset) and computes their pairwise alignment score.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python Concepts Used

1. itertools.product for Coordinate Space Generation
Instead of hardcoding all 15 movement vectors in 4D space or nesting four loops to find them, we use itertools.product.

2. itertools.product for Coordinate Space Generation
Instead of hardcoding all 15 movement vectors in 4D space or nesting four loops to find them, we use itertools.product.

3. Sentinel Values (-float('inf'))
When searching for a maximum score, we need a baseline starting value that is guaranteed to be smaller than any possible calculation.

4. Generator Expressions inside join()
To quickly reconstruct sequences or print aligned results, we use generator expressions directly inside string operations.

---

## Related Problems
-EDTA -- Prerequisite: Pairwise global alignment tracking gaps using standard 2D matrices.
-CLUS -- Advanced: Scaling multiple alignments to hundreds of sequences using progressive alignment algorithms.