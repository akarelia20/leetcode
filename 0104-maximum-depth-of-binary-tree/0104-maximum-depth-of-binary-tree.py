# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case : stop when node is null
        if not root:
            return 0
            # right = self.depth(root.right,count)
            # left= self.depth(root.left,count)
        # adding 1 because current node is not null and "1" is the count for current root node
        return max(self.maxDepth(root.right),self.maxDepth(root.left)) +1
        