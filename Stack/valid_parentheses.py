"""
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

Example:
    Input: s = "()[]{}"
    Output: true
    
    Input: s = "(]"
    Output: false

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s):
    """
    Check if parentheses are valid using a stack.
    
    Args:
        s: String containing parentheses
        
    Returns:
        True if valid, False otherwise
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]
    
    for s, expected in test_cases:
        result = is_valid(s)
        print(f"Input: s = \"{s}\"")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")
