"""
Binary Search

Binary Search is a searching algorithm that finds the position of a target value
within a sorted array by repeatedly dividing the search interval in half.

Time Complexity: O(log n)
Space Complexity: O(1) iterative, O(log n) recursive
"""

def binary_search(arr, target):
    """
    Search for target in sorted array using binary search.
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to search for
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive implementation of binary search.
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to search for
        left: Left boundary
        right: Right boundary
        
    Returns:
        Index of target if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    # Test cases
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    test_cases = [
        (7, 3),
        (1, 0),
        (19, 9),
        (8, -1),
    ]
    
    print("Iterative Binary Search:")
    for target, expected in test_cases:
        result = binary_search(arr, target)
        print(f"Search {target}: index = {result}, expected = {expected}, pass = {result == expected}")
    
    print("\nRecursive Binary Search:")
    for target, expected in test_cases:
        result = binary_search_recursive(arr, target)
        print(f"Search {target}: index = {result}, expected = {expected}, pass = {result == expected}")
