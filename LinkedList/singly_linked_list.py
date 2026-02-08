"""
Linked List Node and Basic Operations

Implementation of a singly linked list with basic operations.

Time Complexity: 
    - Insert at head: O(1)
    - Insert at tail: O(n) without tail pointer
    - Delete: O(n)
    - Search: O(n)

Space Complexity: O(1) for operations
"""

class ListNode:
    """Node in a singly linked list."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, val):
        """Insert a node at the head of the list."""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self, val):
        """Insert a node at the tail of the list."""
        new_node = ListNode(val)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete_value(self, val):
        """Delete the first node with the given value."""
        if not self.head:
            return
        
        if self.head.val == val:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        
        if current.next:
            current.next = current.next.next
    
    def search(self, val):
        """Search for a value in the list."""
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False
    
    def to_list(self):
        """Convert linked list to Python list for display."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result


if __name__ == "__main__":
    # Test linked list operations
    ll = LinkedList()
    
    print("Insert at tail: 1, 2, 3")
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    print(f"List: {ll.to_list()}")
    
    print("\nInsert at head: 0")
    ll.insert_at_head(0)
    print(f"List: {ll.to_list()}")
    
    print("\nSearch for 2:")
    print(f"Found: {ll.search(2)}")
    
    print("\nDelete 2:")
    ll.delete_value(2)
    print(f"List: {ll.to_list()}")
    
    print("\nSearch for 2:")
    print(f"Found: {ll.search(2)}")
