# Key decisions: We use a simple list of floats to represent our expectation coefficients.
# Since we only have 6 elements, a standard zip loop is highly readable and runs in O(1) time.

import sys
from pathlib import Path


def calculate_expected_dominant_offspring(couples: list[int]) -> float:
    """
    Computes the expected number of dominant-phenotype offspring based on
    the counts of the 6 Mendelian parental pairings.
    """
    # Expected dominant offspring per 2 children for each pairing class:
    # 1. AA-AA (2.0), 2. AA-Aa (2.0), 3. AA-aa (2.0)
    # 4. Aa-Aa (1.5), 5. Aa-aa (1.0), 6. aa-aa (0.0)
    coefficients = [2.0, 2.0, 2.0, 1.5, 1.0, 0.0]

    expected_value = sum(count * coeff for count, coeff in zip(couples, coefficients))
    return expected_value


if __name__ == "__main__":
    try:
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_iev.txt"

        if dataset_path.exists():
            # Parse space-separated integers
            data = dataset_path.read_text().strip().split()
            couple_counts = [int(val) for val in data]

            assert len(couple_counts) == 6, "Dataset must contain exactly 6 integers."

            result = calculate_expected_dominant_offspring(couple_counts)
            print(f"{result:.1f}")
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        # Fallback to the Rosalind sample case: 1 0 0 1 0 1
        # Calculation: (1 * 2.0) + (0 * 2.0) + (0 * 2.0) + (1 * 1.5) + (0 * 1.0) + (1 * 0.0) = 3.5
        sample_counts = [1, 0, 0, 1, 0, 1]
        sample_result = calculate_expected_dominant_offspring(sample_counts)
        print("Sample Run Output:")
        print(f"{sample_result:.1f}")
