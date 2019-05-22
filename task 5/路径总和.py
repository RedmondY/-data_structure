# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        target = sum - root.val
        if not root.left and not root.right:
            return target == 0

        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)

