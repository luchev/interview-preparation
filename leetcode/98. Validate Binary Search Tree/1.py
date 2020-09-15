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
        return self.validateBST(root, -math.inf, math.inf)

    # Using intervals
    def validateBST(self, root: TreeNode, lowerBound, upperBound):
        if root is None:
            return True
        if root.val <= lowerBound or upperBound <= root.val:
            return False
        return self.validateBST(root.left, lowerBound, root.val) and self.validateBST(root.right, root.val, upperBound)
