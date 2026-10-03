# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif (p is not None and q is None) or (p is None and q is not None):
            return False

        leftValid = p.val == q.val
        rightValid = p.val == q.val

        if p.left is not None and q.left is not None:
            leftValid = self.isSameTree(p.left,q.left)
        elif p.left is not None or q.left is not None:
            leftValid = False
        
        if p.right is not None and q.right is not None:
            rightValid = self.isSameTree(p.right,q.right)
        elif p.right is not None or q.right is not None:
            rightValid = False
        
        return leftValid and rightValid