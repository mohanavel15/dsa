"""
Binary Tree Node and Basic Operations

Implementation of a binary tree with basic traversals.

Traversals:
    - Inorder (Left, Root, Right)
    - Preorder (Root, Left, Right)
    - Postorder (Left, Right, Root)
    - Level Order (BFS)

Time Complexity: O(n) for all traversals
Space Complexity: O(h) for recursive traversals, O(w) for level order
"""

from collections import deque


class TreeNode:
    """Node in a binary tree."""
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    """Inorder traversal: Left -> Root -> Right"""
    result = []
    
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(root)
    return result


def preorder_traversal(root):
    """Preorder traversal: Root -> Left -> Right"""
    result = []
    
    def preorder(node):
        if not node:
            return
        result.append(node.val)
        preorder(node.left)
        preorder(node.right)
    
    preorder(root)
    return result


def postorder_traversal(root):
    """Postorder traversal: Left -> Right -> Root"""
    result = []
    
    def postorder(node):
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        result.append(node.val)
    
    postorder(root)
    return result


def level_order_traversal(root):
    """Level order traversal (BFS)"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


if __name__ == "__main__":
    # Create a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Binary Tree Traversals:")
    print(f"Inorder:    {inorder_traversal(root)}")
    print(f"Preorder:   {preorder_traversal(root)}")
    print(f"Postorder:  {postorder_traversal(root)}")
    print(f"Level Order: {level_order_traversal(root)}")
