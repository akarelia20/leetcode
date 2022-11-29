# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.recursive(root,result)
        return result
        
    def recursive(self,root,result):
        if root != None:
            result.append(root.val)
            self.recursive(root.left,result)
            self.recursive(root.right,result)

            