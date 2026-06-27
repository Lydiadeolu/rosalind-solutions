# Key decisions: Python handles arbitrarily large scalar integers automatically, meaning
# we don't have to worry about numerical integer overflow as the sequence scales.
# Using a simple iterative swap loop optimizes space complexity down to O(1) memory.


def solve_fib(n: int, k: int) -> int:
    """
    Computes the total rabbit pairs after n months with litter size k.
    """
    # Handle baseline boundary cases
    if n == 1 or n == 2:
        return 1
        
    # Set up sliding variables for bottom-up dynamic programming
    parent_generation = 1  # F_1
    current_generation = 1 # F_2
    
    for _ in range(3, n + 1):
        # Next term = Adults alive from previous month + (Fertile grandparents * litter yield)
        next_generation = current_generation + (parent_generation * k)
        
        # Slide state values forward in the execution cycle
        parent_generation = current_generation
        current_generation = next_generation
        
    return current_generation

if __name__ == "__main__":
    try:
        with open("stronhold/Dataset/rosalind_fib.txt") as file:
            # Read lines and strip out trailing newline spacing markers
            n, k = map(int, file.read().strip().split())
            print(solve_fib(n, k))
            
    except FileNotFoundError:
        # Fallback textbook sample test case
        print(solve_fib(5, 3))