"""
Stack Implementation using List

A stack is a linear data structure that follows the LIFO (Last In First Out) principle.

Operations:
    - push(item): Add item to top - O(1)
    - pop(): Remove and return top item - O(1)
    - peek(): Return top item without removing - O(1)
    - is_empty(): Check if stack is empty - O(1)
    - size(): Return number of items - O(1)

Space Complexity: O(n)
"""

class Stack:
    """Stack implementation using Python list."""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
    
    def __str__(self):
        """String representation of stack."""
        return f"Stack({self.items})"


if __name__ == "__main__":
    # Test stack operations
    stack = Stack()
    
    print("Push: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(f"Size: {stack.size()}")
    
    print(f"\nPeek: {stack.peek()}")
    
    print(f"\nPop: {stack.pop()}")
    print(stack)
    
    print(f"\nPop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")
    print(f"Is empty: {stack.is_empty()}")
