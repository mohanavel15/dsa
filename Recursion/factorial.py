"""
Factorial (Recursion)

Calculate factorial of a number using recursion.

Time Complexity: O(n)
Space Complexity: O(n) due to call stack
"""

def factorial(n):
    """
    Calculate factorial recursively.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def factorial_iterative(n):
    """
    Calculate factorial iteratively.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
    ]
    
    print("Factorial - Recursive:")
    for n, expected in test_cases:
        result = factorial(n)
        print(f"{n}! = {result}, expected = {expected}, pass = {result == expected}")
    
    print("\nFactorial - Iterative:")
    for n, expected in test_cases:
        result = factorial_iterative(n)
        print(f"{n}! = {result}, expected = {expected}, pass = {result == expected}")
