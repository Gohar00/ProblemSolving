"""Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
"""Time comp. O(n)"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: [TreeNode]):
         lst = []
         tmp = []

         while root or tmp:
             while root:
                 tmp.append(root)
                 root = root.left
             root = tmp.pop()
             lst.append(root.val)
             root = root.right
         return lst