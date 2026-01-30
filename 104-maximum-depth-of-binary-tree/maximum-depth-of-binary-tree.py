class Solution:
    def maxDepth(self, root):
        # base case
        if root is None:
            return 0
        
        # left aur right subtree ki depth nikalo
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # current node + maximum of left & right
        return 1 + max(left_depth, right_depth)
