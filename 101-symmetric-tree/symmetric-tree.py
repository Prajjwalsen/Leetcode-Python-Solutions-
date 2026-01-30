# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def chk(a,b):
            if (a==None and b==None):
                return True
            if (a==None or b==None):
                return False 
            return (a.val==b.val) and chk(a.left,b.right) and chk(a.right,b.left)
        return chk(root,root)