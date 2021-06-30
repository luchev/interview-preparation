# Complexity (n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        def dfs(root):
            if root is None:
                return 0
            
            nonlocal result
            left = dfs(root.left)
            right = dfs(root.right)
            current = 0
            if root == p or root == q:
                current = 1
            if current + left + right == 2:
                result = root
                
            if current + left + right > 0:
                return 1
            return 0
        
        dfs(root)
        return result