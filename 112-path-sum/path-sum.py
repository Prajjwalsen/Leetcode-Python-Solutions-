# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root==None):
            return False 
        def chk(root,target):
            if(root==None):
                return False 
            if(root.val==target and root.left==None and root.right==None):
                return True

            return chk(root.left,target-root.val) or chk(root.right,target-root.val)
        return chk(root,targetSum)

        