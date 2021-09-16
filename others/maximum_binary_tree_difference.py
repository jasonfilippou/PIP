'''
Find the maximum difference between two nodes in a binary tree. Note that the binary tree does not necessarily have
to be a BST.
'''

from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

def greatest_difference_one(root: Optional[TreeNode]) -> int:

    def find_max(root: Optional[TreeNode]) -> int:
        return max(root.val, find_max(root.left), find_max(root.right)) if root else float("-inf")

    def find_min(root: Optional[TreeNode]) -> int:
        return min(root.val, find_min(root.left), find_min(root.right)) if root else float("inf")

    return find_max(root) - find_min(root)

def greatest_difference_two(root: Optional[TreeNode]):
    # This one does the same but only scanning the tree once. It won't work in Python 2 because it doesn't have `nonlocal` keyword :(

    def traverse(root: Optional[TreeNode]):
        nonlocal min_val, max_val
        if root:
            max_val = max(max_val, root.val)
            min_val = min(min_val, root.val)
            traverse(root.left)
            traverse(root.right)

    min_val = float("inf")
    max_val = float("-inf")         # Notice the "opposite" initialization with respect to the semantics of the var names!
    traverse(root)
    return max_val - min_val if root is not None else float("inf")



if __name__ == '__main__':
    ''' 
                      10

              20              2

         65       9       10

                            11
    '''

    root = TreeNode(10)
    root.left = TreeNode(20)
    root.left.right = TreeNode(9)
    root.right = TreeNode(2)
    root.left.left = TreeNode(65)
    root.right.left = TreeNode(10)
    root.right.left.right = TreeNode(11)
    print(greatest_difference_one(root))
    print(greatest_difference_two(root))