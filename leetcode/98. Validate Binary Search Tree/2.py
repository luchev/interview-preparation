# Complexity(n = nodes in tree)
# Time complexity: O(n)
# Space complexity: O(n) memory on the stack for the recursion

import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.min = -math.inf
        return self.validateBST(root)
    # Inorder traversal
    def validateBST(self, root: TreeNode):
        if root is None:
            return True
        
        if not self.validateBST(root.left):
            return False
        
        if root.val <= self.min:
            return False
        self.min = root.val
        
        return self.validateBST(root.right)
