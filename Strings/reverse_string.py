"""
Reverse String

Write a function that reverses a string in-place.

Example:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverse_string(s):
    """
    Reverse a string in-place using two pointers.
    
    Args:
        s: List of characters
        
    Returns:
        None (modifies s in-place)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]
    
    for s, expected in test_cases:
        original = s.copy()
        reverse_string(s)
        print(f"Input: s = {original}")
        print(f"Output: {s}")
        print(f"Expected: {expected}")
        print(f"Pass: {s == expected}\n")
