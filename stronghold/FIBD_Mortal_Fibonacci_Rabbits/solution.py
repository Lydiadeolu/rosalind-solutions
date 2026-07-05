# Key decisions: We use a list-based sliding window shift operation to simulate 
# time steps. This maintains an O(n) runtime complexity and keeps memory bounds 
# minimal at O(m). Paths are resolved via cross-platform `pathlib`.

import sys
from pathlib import Path

def solve_mortal_rabbits(n: int, m: int) -> int:
    """
    Computes the remaining rabbit population at month n given a lifespan of m.
    """
    # Initialize age tracks: index i represents pairs that are i months old
    # Track sizes up to index m-1 (maximum age before death)
    age_cohorts = [0] * m
    age_cohorts[0] = 1  # Month 1: One newborn pair
    
    for month in range(2, n + 1):
        # 1. Total reproductive pairs = sum of cohorts aged 1 month or older
        newborns = sum(age_cohorts[1:])
        
        # 2. Shift the conveyor belt right (aging everything by 1 month)
        # The last element age_cohorts[-1] drops off naturally (death)
        age_cohorts = [newborns] + age_cohorts[:-1]
        
    return sum(age_cohorts)

if __name__ == "__main__":
    try:
        # Cross-platform relative workspace path parsing using Pathlib
        current_dir = Path(__file__).resolve().parent
        dataset_path = current_dir / ".." / "Dataset" / "rosalind_fibd.txt"
        
        if dataset_path.exists():
            data = dataset_path.read_text().strip().split()
            n_months = int(data[0])
            lifespan = int(data[1])
            print(solve_mortal_rabbits(n_months, lifespan))
        else:
            raise FileNotFoundError
            
    except FileNotFoundError:
        # Fallback textbook sample test case simulation (n=6, m=3)
        # Expected Output: 4
        print(solve_mortal_rabbits(6, 3))
