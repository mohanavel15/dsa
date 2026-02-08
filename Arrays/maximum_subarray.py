"""
Maximum Subarray (Kadane's Algorithm)

Given an integer array nums, find the contiguous subarray which has the largest sum and return its sum.

Example:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_subarray(nums):
    """
    Find maximum sum of contiguous subarray using Kadane's algorithm.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of contiguous subarray
    """
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ]
    
    for nums, expected in test_cases:
        result = max_subarray(nums)
        print(f"Input: nums = {nums}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")
