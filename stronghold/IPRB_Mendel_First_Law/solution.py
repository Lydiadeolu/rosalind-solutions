# Key decisions: Calculating the complement event (recessive phenotype emergence) 
# reduces conditional routing overhead. We handle the combinatorial selections sequentially 
# using simple float arithmetic to guarantee O(1) execution space and execution speed.


def calculate_dominant_probability(k: int, m: int, n: int) -> float:
    """
    Computes the probability that two randomly selected organisms produce 
    an offspring displaying a dominant phenotype.
    """
    t = k + m + n
    
    # Calculate the total number of unique mating pair combinations
    total_pairs = t * (t - 1)
    
    # Calculate weighted combinations that yield recessive (xx) offspring
    # Note: We omit the combination division over 2 because it cancels out in the ratio
    recessive_from_mm = m * (m - 1) * 0.25  # Hetero x Hetero (1/4 chance)
    recessive_from_mn = m * n * 0.50 * 2    # Hetero x Recessive (1/2 chance, ordered pairs)
    recessive_from_nn = n * (n - 1) * 1.00  # Recessive x Recessive (100% chance)
    
    total_recessive_prob = (recessive_from_mm + recessive_from_mn + recessive_from_nn) / total_pairs
    
    return 1 - total_recessive_prob

if __name__ == "__main__":
    try:
        with open("stronghold/Dataset/rosalind_iprb.txt") as file: 
            k, m, n = map(int, file.read().strip().split())
            print(f"{calculate_dominant_probability(k, m, n):.5f}")
            
    except FileNotFoundError:
        # Fallback textbook sample test case (2 dominant, 2 hetero, 2 recessive)
        print(f"{calculate_dominant_probability(2, 2, 2):.5f}")