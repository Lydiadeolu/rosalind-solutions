# Key decisions: Using a loop with a conditional check is clear and instructive. 
# While this can also be solved using mathematical series formulas or step-wise 
# ranges (e.g., range(start, b+1, 2)), a standard loop explicitly fulfills 
# the problem's goal of practicing conditions and loops.

def sum_odds_in_range(a, b):
    total_sum = 0
    # b + 1 ensures that 'b' is included in our iteration range
    for num in range(a, b + 1):
        if num % 2 != 0:  # Check if the number is odd
            total_sum += num
    return total_sum

if __name__ == "__main__":
    try:
        with open("python_village/Dateset/rosalind_ini4.txt") as file:
            # Parse the two space-separated integers
            a, b = map(int, file.read().strip().split())
            print(sum_odds_in_range(a, b))
            
    except FileNotFoundError:
        # Fallback test example from Rosalind description
        print(sum_odds_in_range(100, 200))
