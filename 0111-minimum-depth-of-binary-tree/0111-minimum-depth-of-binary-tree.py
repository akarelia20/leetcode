# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = collections.deque()
        queue.append((root,1))
        
        while queue:
            node, depth = queue.popleft()
            
            if node.right == None and node.left== None:
                return depth
            if node.right:
                queue.append((node.right, depth+1))
            if node.left:
                queue.append((node.left, depth+1))
                
# def minDepthDFS(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
        
#         if root.right == None and root.left == None:
#             return 1
#         if root.right and not root.left:
#             return 1+(self.minDepth(root.right))
#         if root.left and not root.right:
#             return 1+(self.minDepth(root.left))
        
#         return 1+min(self.minDepth(root.right), self.minDepth(root.left))