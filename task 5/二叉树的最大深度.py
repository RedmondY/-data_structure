# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.helper(root.left, 0), self.helper(root.right, 0)) + 1

    def helper(self, root, depth):
        if not root:
            return depth

        depth += 1
        return max(self.helper(root.left, depth), self.helper(root.right, depth))


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
