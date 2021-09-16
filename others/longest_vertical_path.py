from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


def longest_vertical_path(root: TreeNode) -> int:
    max_len_path = 0

    def helper(root: TreeNode, parent_key: int, current_len: int):
        nonlocal max_len_path
        if root:
            next_len = current_len + 1 if root.val == parent_key else 0
            if next_len > max_len_path:
                max_len_path = next_len
            helper(root.left, root.val, next_len)
            helper(root.right, root.val, next_len)

    helper(root, None, 0)

    return max_len_path

if __name__ == '__main__':
    '''
    
    Tree of my own:
                    60
                  /    \
                 /      \
                /        \
               /          \
             40            70
               \          /  \
                \        /    \
                 55    60      60
                /     /  \     /
               55    70  75  60
              /  \
            70    55
            
    Answer should be '2', for the vertical path from 55 to 55. Our paths are counted in terms of edges.   
    '''

    # Inserting the nodes in level-order:
    root = TreeNode(60)
    root.left = TreeNode(40)
    root.right = TreeNode(70)
    root.left.right = TreeNode(55)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(60)
    root.left.right.left = TreeNode(55)
    root.right.left.left = TreeNode(70)
    root.right.left.right = TreeNode(75)
    root.right.right = TreeNode(60)
    root.right.right.left = TreeNode(60)

    print(f"Longest vertical path in tree is: {longest_vertical_path(root)}.")