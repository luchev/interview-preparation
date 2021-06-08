# Complexity (n = input length or number of nodes in the output tree)
# Time complexity: O(1)
# Space complexity: O(n)

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorderIndices = {}
        for i, x in enumerate(inorder):
            inorderIndices[x] = i
            
        def build(left, right):
            if left > right:
                return None
            
            nonlocal preorderIndex
            root = TreeNode(preorder[preorderIndex])
            preorderIndex += 1
            root.left = build(left, inorderIndices[root.val] - 1)
            root.right = build(inorderIndices[root.val] + 1, right)
            
            return root
        
        preorderIndex = 0
        return build(0, len(preorder) - 1)
