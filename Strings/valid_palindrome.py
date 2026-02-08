"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward.

Example:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_palindrome(s):
    """
    Check if a string is a valid palindrome.
    
    Args:
        s: Input string
        
    Returns:
        True if palindrome, False otherwise
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ]
    
    for s, expected in test_cases:
        result = is_palindrome(s)
        print(f"Input: s = \"{s}\"")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")
