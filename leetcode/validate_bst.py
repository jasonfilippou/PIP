# https://leetcode.com/problems/validate-binary-search-tree/
#
#
#     A naive recursive solution might blow up the stack, because I have as many as 10,000 nodes.
#  I will therefore need an approach based on my own stack. Every time I go to the left, I push the child in the stack,
#  updating the current right bound to the current node's value while maintaining the left (small) bound that I was pushed with.
#  Respectively, when I go to the right, I update the  current left (small) bound to the current node's value, while maintaining
#  the right (large) bound that I was pushed with.
#
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, None, None)]
        while len(stack) != 0:
            node_and_bounds = stack.pop()  # removes the last item
            node = node_and_bounds[0]
            lower_bound = node_and_bounds[1]
            upper_bound = node_and_bounds[2]
            # Ensure the current value is within bounds.
            if lower_bound is not None and node.val <= lower_bound:
                return False
            elif upper_bound is not None and node.val >= upper_bound:
                return False
            # The order of the subsequent if conditions will also determine the traversal:
            # r->L->R or r->R->L. It is important that we push the correct information about current bounds.
            if node.right is not None:
                stack.append((node.right, node.val,
                              upper_bound))  # Pushing right 1st means we will examine the right subtree 2nd. Upper bound does not change.
            if node.left is not None:
                stack.append((node.left, lower_bound, node.val))
        return True


if __name__ == '__main__':
    s = Solution()
    # Let's run Leetcode's test cases first
    # (1) A valid 3 - node BST
    r = TreeNode(2)
    r.left = TreeNode(1)
    r.right = TreeNode(3)
    print(s.isValidBST(r))

    # (2) An invalid 5-node BST.

    r = TreeNode(5)
    r.left = TreeNode(1)
    r.right = TreeNode(4)
    r.right.left = TreeNode(3)
    r.right.right = TreeNode(6)
    print(s.isValidBST(r))

    # (3) A perfectly structured 3 - level BST found invalid at the rightmost leaf
    r = TreeNode(5)
    r.left = TreeNode(-5)
    r.left.left = TreeNode(-6)
    r.left.right = TreeNode(2)
    r.right = TreeNode(10)
    r.right.left = TreeNode(8)
    r.right.right = TreeNode(1)     # Fly in the soup
    print(s.isValidBST(r))

    # (4) Stress test left

    root = TreeNode(10000)
    r = root
    for i in range(9999, 0, -1):
        r.left = TreeNode(i)
        r = r.left
    r.left = TreeNode(root.val + 1)       # Explicitly making the tree an invalid BST.
    r = root
    print(s.isValidBST(r))

    # (5) Stress test right

    root = TreeNode(1)
    r = root
    for i in range(2, 10001):
        r.right = TreeNode(i)
        r = r.right
    r.right = TreeNode(root.val + 1)      # Explicitly making the tree an invalid BST.
    r = root
    print(s.isValidBST(r))

    # Test cases I failed on LeetCode:
    # (6)
    r = TreeNode(1)
    r.right = TreeNode(1)                 # Duplicate, not a BST.
    print(s.isValidBST(r))

    # (7)
    r = TreeNode(5)
    r.left = TreeNode(4)
    r.right = TreeNode(6)
    r.right.left = TreeNode(3)          # 3 on the right of 7; this can't be a BST
    r.right.right = TreeNode(7)