# Complexity (n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        succ = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                succ = root
                root = root.left
        
        return succ
