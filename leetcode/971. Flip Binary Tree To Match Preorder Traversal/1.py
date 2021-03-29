# Complexity (n = nodes in the tree = length of voyage)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        if not root:
            return root
        
        vIndex = 0
        swaps = []
        valid = True
        
        def dfs(root: TreeNode):
            if not root:
                return
            
            nonlocal swaps
            nonlocal vIndex
            nonlocal valid
            
            if voyage[vIndex] != root.val:
                valid = False
                return
            
            vIndex += 1
            if root.left and root.left.val != voyage[vIndex]:
                root.left, root.right = root.right, root.left
                swaps.append(root.val)

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        if valid:
            return swaps
        else:
            return [-1]
