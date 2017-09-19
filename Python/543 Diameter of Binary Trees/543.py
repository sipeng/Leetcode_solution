# ideas:
# - Recursion
# - Note: the longest path may not include the root
# - Keep track of current max, and update it each time we call maxdepth()
# - Store the current max as self.diameter


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.maxdepth(root)
        return self.diameter
    
    def maxdepth(self, root):
        if root is None:
            return 0
        leftd = self.maxdepth(root.left)
        rightd = self.maxdepth(root.right)
        maxd = max(leftd, rightd)
        self.diameter = max(leftd+rightd, self.diameter)
        return maxd + 1