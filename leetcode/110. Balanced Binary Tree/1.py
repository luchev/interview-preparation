# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

import math
from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if height(root) < math.inf:
            return True
        return False


@cache
def height(root: TreeNode):
    if root is None:
        return 0
    height_left = height(root.left)
    height_right = height(root.right)

    if abs(height_left - height_right) > 1:
        return math.inf

    return 1 + max(height_left, height_right)
