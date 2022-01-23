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
    def connect(self, root):
        
        def levels(root):
            if root is None or root.left is None:
                return root
        
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left
            
            levels(root.left)
            levels(root.right)
            return root
    
        return levels(root)
        
#---------------Solution Stats---------------#
#          Test Cases Passed: 39/39
#Runtime: 50ms (Top 15% of Python Submissions)
#Memory Usage: 16.3MB (Top 25% of Python Submissions)
#--------------------------------------------#
