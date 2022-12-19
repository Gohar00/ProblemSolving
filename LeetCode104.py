"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.
"""
"""Time Comp O(N)"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: [TreeNode]):

    if root == None:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(8)
root.right.left.right = TreeNode(7)
print(maxDepth(root))
