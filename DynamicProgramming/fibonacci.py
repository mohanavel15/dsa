"""
Fibonacci Numbers

Calculate Fibonacci numbers using different approaches.

Time Complexity: 
    - Recursive: O(2^n)
    - Dynamic Programming: O(n)
    - Iterative: O(n)

Space Complexity:
    - Recursive: O(n)
    - Dynamic Programming: O(n)
    - Iterative: O(1)
"""

def fibonacci_recursive(n):
    """Calculate nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dp(n):
    """Calculate nth Fibonacci number using dynamic programming."""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_iterative(n):
    """Calculate nth Fibonacci number iteratively."""
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55),
    ]
    
    print("Fibonacci - Iterative (Most Efficient):")
    for n, expected in test_cases:
        result = fibonacci_iterative(n)
        print(f"fib({n}) = {result}, expected = {expected}, pass = {result == expected}")
    
    print("\nFibonacci - Dynamic Programming:")
    for n, expected in test_cases:
        result = fibonacci_dp(n)
        print(f"fib({n}) = {result}, expected = {expected}, pass = {result == expected}")
    
    print("\nFibonacci - Recursive (Slow for large n):")
    for n, expected in test_cases[:3]:  # Only test small values
        result = fibonacci_recursive(n)
        print(f"fib({n}) = {result}, expected = {expected}, pass = {result == expected}")
