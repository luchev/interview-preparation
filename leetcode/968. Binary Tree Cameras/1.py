# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        result = 0
        covered = set([None])
        def dfs(node, parent):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                nonlocal result
                
                if parent is None and node not in covered or node.left not in covered or node.right not in covered:
                        result += 1
                        covered.update([node, parent, node.left, node.right])
    
        dfs(root, None)
        return result