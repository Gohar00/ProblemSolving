"""Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
"""Time comp. O(n)"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: TreeNode):
        lst = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)

        inorder(root)
        return lst
