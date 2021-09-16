# This file will only contain traversals using a custom stack. Recursive ones are easy.

from __future__ import annotations      # To allow the TreeNode constructor to successfully parse arguments of the enclosing type.


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode):
    stack = [root]
    while stack:
        node = stack.pop()
        visit(node)                         # pre-visit
        if node.right:
            stack.append(node.right)        # Pushing the right node first makes it be processed second, which is what pre-order traversal does.
        if node.left:
            stack.append(node.left)


def anti_preorder(root: TreeNode):          # A kind of stupid traversal that is basically r->R->L. Not really used in BSTs.
    stack = [root]
    while stack:
        node = stack.pop()
        visit(node)                         # pre-visit
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)        # Pushing the right node second makes it be processed first!


def inorder(root: TreeNode):
    stack = []
    curr = root
    while stack or curr is not None:
        while curr is not None:             # First go as left as you can.
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()                  # When you can't go further left, pop your parent and visit him.
        visit(curr)
        curr = curr.right                   # Afterwards, go right if you can, and rinse / repeat.



def anti_inorder(root: TreeNode):            # Same idea as "anti-preorder": rRl
    stack = []
    curr = root
    while stack or curr is not None:
        while curr is not None:             # First go as left as you can.
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()                  # When you can't go further left, pop your parent and visit him.
        visit(curr)
        curr = curr.left


def visit(node: TreeNode):
    print(node.val)


if __name__ == '__main__':
    ''' 
                          10

                  20              2

             65       9       10
             
                                11
                        
    '''
    #
    root = TreeNode(10)
    root.left = TreeNode(20)
    root.right = TreeNode(2)
    root.left.left = TreeNode(65)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.left.right = TreeNode(11)
    print("Pre-order:")
    preorder(root)
    print("Anti-preorder:")
    anti_preorder(root)
    print("Inorder:")
    inorder(root)
    print("Anti-inorder:")
    anti_inorder(root)
