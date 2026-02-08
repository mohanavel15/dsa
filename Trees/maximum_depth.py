"""
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Time Complexity: O(n)
Space Complexity: O(h) where h is height
"""

class TreeNode:
    """Node in a binary tree."""
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    """
    Find the maximum depth of a binary tree.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        Maximum depth
    """
    if not root:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    # Test case: Tree with depth 3
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    result = max_depth(root)
    print(f"Maximum depth: {result}")
    print(f"Expected: 3")
    print(f"Pass: {result == 3}")
