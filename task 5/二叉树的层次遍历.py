# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        tmp = [root]
        while tmp:
            level = []
            next_tmp = []
            for node in tmp:

                level.append(node.val)
                if node.left:
                    next_tmp.append(node.left)
                if node.right:
                    next_tmp.append(node.right)
            result.append(level)
            tmp = next_tmp

        return result
    
