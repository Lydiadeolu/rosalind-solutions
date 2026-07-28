# Key decisions: We strictly utilize `math.log10()` to compile the probability weights
# additively. This completely shields the execution script from floating-point
# underflow degradation, ensuring absolute numerical precision for long sequences.

import sys
import math
from pathlib import Path


def compute_log_probabilities(dna_string: str, gc_array: list[float]) -> list[float]:
    """
    Computes the log-probability of a DNA string given an array of GC-content thresholds.
    """
    results = []

    for gc in gc_array:
        # Precompute the individual log10 probabilities for both base families
        log_gc = math.log10(gc / 2.0)
        log_at = math.log10((1.0 - gc) / 2.0)

        total_log_prob = 0.0

        # Accumulate the log weights additively instead of multiplying raw decimals
        for base in dna_string:
            if base in ("G", "C"):
                total_log_prob += log_gc
            elif base in ("A", "T"):
                total_log_prob += log_at

        results.append(round(total_log_prob, 3))

    return results


if __name__ == "__main__":
    try:
        # Cross-platform relative file path resolution using Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_prob.txt"

        if dataset_path.exists():
            lines = dataset_path.read_text().strip().splitlines()
            target_dna = lines[0].strip().upper()
            gc_content_floats = [float(x) for x in lines[1].strip().split()]

            # Compute and output space-separated log values
            output_array = compute_log_probabilities(target_dna, gc_content_floats)
            print(" ".join(map(str, output_array)))
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        # Fallback textbook sample simulation parameters
        sample_dna = "ACGATACAA"
        sample_gc = [0.123, 0.456, 0.789]

        output_array = compute_log_probabilities(sample_dna, sample_gc)
        print("Sample Run Output:", " ".join(map(str, output_array)))
