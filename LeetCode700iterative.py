"""You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the
subtree rooted with that node. If such a node does not exist, return null."""
"""Time comp O(n)"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: [TreeNode], val: int):

        if root is None:
            return None
        while root is not None:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None
