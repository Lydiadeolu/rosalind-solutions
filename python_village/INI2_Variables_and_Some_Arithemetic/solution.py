def solve_hypotenuse_squared(a, b ):
    return (int (a) ** 2) + ( int (b) ** 2)

# Example usage with test values:
if __name__ == "__main__":
    # Substitute with your actual Rosalind dataset values
    a = input("what is the value of a? ") 

    b = input("what is the value of b? ")

    print(solve_hypotenuse_squared(a, b))