
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node, lower, upper):
        if not node:
            return True

        if node.val > lower and node.val < upper:
            return self.helper(node.left, lower, node.val) and self.helper(node.right, node.val, upper)
        else:
            return False
