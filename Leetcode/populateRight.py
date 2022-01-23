"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        
        self.dfs(root, result)
        return result

    def dfs(self, root, result):
        if root is None:
                return
        self.dfs(root.left, result)
        result.append(root.val)
        self.dfs(root.right, result)
        return result
        
#---------------Solution Stats---------------#
#          Test Cases Passed: 70/70
#Runtime: 20.2ms (Top 50% of Python Submissions)
#Memory Usage: 13.2MB (Top 5% of Python Submissions)
#--------------------------------------------#
