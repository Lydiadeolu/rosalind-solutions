# Key decisions: We compute the exact binomial cumulative distribution manually
# using `math.comb()` for combinations and standard float exponentiation. This avoids
# loading massive external scientific libraries like Scipy while ensuring O(2^k) safety.

import sys
import math
from pathlib import Path


def independent_alleles_prob(k: int, N: int) -> float:
    """
    Calculates the probability that at least N organisms are Aa Bb at generation k
    using the Binomial Probability Mass Function (PMF).
    """
    total_population = 2**k
    success_prob = 0.25
    failure_prob = 0.75

    at_least_N_prob = 0.0

    # Sum the probabilities from N up to the entire population limit
    for x in range(N, total_population + 1):
        # Binomial formula: comb(n, x) * (p^x) * (q^(n-x))
        combinations = math.comb(total_population, x)
        pmf_value = (
            combinations * (success_prob**x) * (failure_prob ** (total_population - x))
        )
        at_least_N_prob += pmf_value

    return round(at_least_N_prob, 3)


if __name__ == "__main__":
    try:
        # Cross-platform relative file path resolution using Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_lia.txt"

        if dataset_path.exists():
            content = dataset_path.read_text().strip().split()
            k_gen = int(content[0])
            n_target = int(content[1])

            # Print the final rounded probability value
            print(independent_alleles_prob(k_gen, n_target))
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        # Fallback textbook sample simulation parameters
        sample_k, sample_N = 2, 1
        # Expected Output: 0.684
        print("Sample Run Output:", independent_alleles_prob(sample_k, sample_N))
