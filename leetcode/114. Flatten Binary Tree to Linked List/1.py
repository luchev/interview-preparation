# Complexity (n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        
        ptr = root
        while ptr is not None:
            if ptr.left is not None:
                rightMost = ptr.left
                while rightMost.right is not None:
                    rightMost = rightMost.right
                rightMost.right = ptr.right
                
                ptr.right = ptr.left
                ptr.left = None
            ptr = ptr.right