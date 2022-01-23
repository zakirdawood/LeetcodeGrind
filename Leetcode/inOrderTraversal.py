# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        
        def dfs(root, result):
            if root is None:
                return
            dfs(root.left, result)
            result.append(root.val)
            dfs(root.right, result)
            return result
        
        dfs(root, result)
        return result