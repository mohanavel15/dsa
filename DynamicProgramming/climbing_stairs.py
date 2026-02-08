"""
Climbing Stairs (Dynamic Programming)

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Time Complexity: O(n)
Space Complexity: O(1)
"""

def climb_stairs(n):
    """
    Calculate number of ways to climb stairs.
    
    Args:
        n: Number of steps
        
    Returns:
        Number of distinct ways
    """
    if n <= 2:
        return n
    
    # At each step, ways = ways(n-1) + ways(n-2)
    prev2, prev1 = 1, 2
    
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ]
    
    for n, expected in test_cases:
        result = climb_stairs(n)
        print(f"n = {n}: {result} ways, expected = {expected}, pass = {result == expected}")
