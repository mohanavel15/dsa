"""
Reverse Linked List

Reverse a singly linked list.

Example:
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
    Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    """Node in a singly linked list."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """
    Reverse a linked list iteratively.
    
    Args:
        head: Head of the linked list
        
    Returns:
        New head of the reversed list
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def list_to_array(head):
    """Convert linked list to array for display."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def array_to_list(arr):
    """Convert array to linked list."""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


if __name__ == "__main__":
    # Test case
    print("Original list: [1, 2, 3, 4, 5]")
    head = array_to_list([1, 2, 3, 4, 5])
    
    reversed_head = reverse_list(head)
    result = list_to_array(reversed_head)
    
    print(f"Reversed list: {result}")
    print(f"Expected: [5, 4, 3, 2, 1]")
    print(f"Pass: {result == [5, 4, 3, 2, 1]}")
