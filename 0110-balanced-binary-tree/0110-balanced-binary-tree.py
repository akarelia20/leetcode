# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #inner function returns "t/f" and height of the left and right sub-tree
        def checkHeight(root):
            if root is None:
                return [True, 0]
            left = checkHeight(root.left)
            right = checkHeight(root.right)
            # balance reeturns bool which is at index 0
            balance = left[0] and right [0] and abs(left[1]-right[1])<=1
            
            return [balance, 1+ max(left[1], right[1])]
        
        return checkHeight(root)[0]