"""Given a binary tree, determine if it is
height-balanced.
"""
"""Time Comp O(N)"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:

        if root == None:
            return True

        def check_depth(root):
            if not root:
                return 0

            left_depth = check_depth(root.left)
            right_depth = check_depth(root.right)

            max_depth = 1 + max(left_depth, right_depth)

            if abs(left_depth - right_depth) > 1 or left_depth == None or right_depth == None:
                return None
            return max_depth

        if check_depth(root) == None:
            return False
        return True

