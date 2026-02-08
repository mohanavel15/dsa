"""
Two Sum Problem

Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    """
    Find two numbers that add up to target using hash map approach.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    
    for nums, target, expected in test_cases:
        result = two_sum(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")
