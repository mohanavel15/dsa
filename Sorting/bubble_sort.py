"""
Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.

Time Complexity: O(n²) average and worst case, O(n) best case
Space Complexity: O(1)
"""

def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps were made, array is sorted
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ]
    
    for arr, expected in test_cases:
        result = bubble_sort(arr)
        print(f"Input:    {arr}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"Pass: {result == expected}\n")
