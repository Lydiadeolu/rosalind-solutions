# Key decisions:
# 1. We leverage Python's itertools library to cleanly compute the Cartesian product of signs
#    and the permutations of elements without writing deeply nested recursive backtracking loops.
# 2. Performance is optimized for the upper bound (n=6) as 2^6 * 6! = 46,080 states,
#    which computes in less than 0.1 seconds in Python.

import sys
from itertools import permutations, product
from pathlib import Path


def generate_signed_permutations(n: int) -> list[tuple[int, ...]]:
    """
    Generates all signed permutations of length n.
    Returns a list of tuples containing the signed integers.
    """
    results = []

    # Step 1: Get all absolute order permutations of 1 to n
    base_perms = list(permutations(range(1, n + 1)))

    # Step 2: Generate all possible sign vector matrices (e.g., (1, -1, 1))
    sign_profiles = list(product([1, -1], repeat=n))

    # Step 3: Combine base permutations with the sign configurations
    for perm in base_perms:
        for signs in sign_profiles:
            # Pairwise multiplication of the element by its designated sign
            signed_perm = tuple(item * sign for item, sign in zip(perm, signs))
            results.append(signed_perm)

    return results


if __name__ == "__main__":
    try:
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_sign.txt"

        if dataset_path.exists():
            n = int(dataset_path.read_text().strip())

            signed_perms = generate_signed_permutations(n)

            # Print the total count followed by each permutation
            print(len(signed_perms))
            for perm in signed_perms:
                print(" ".join(map(str, perm)))
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        # Fallback simulation for n=2 (Expected Output: 2^2 * 2! = 8 elements)
        print("Sample run for n=2:")
        sample_results = generate_signed_permutations(2)
        print(len(sample_results))
        for perm in sample_results:
            print(" ".join(map(str, perm)))
