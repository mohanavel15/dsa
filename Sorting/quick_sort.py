"""
Quick Sort

Quick Sort is a divide-and-conquer algorithm that picks an element as pivot
and partitions the array around the pivot.

Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n) due to recursion
"""

def quick_sort(arr):
    """
    Sort an array using quick sort algorithm.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ]
    
    for arr, expected in test_cases:
        result = quick_sort(arr)
        print(f"Input:    {arr}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")
