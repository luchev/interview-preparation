# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.min_depth = math.inf
        self.dfs(root, 1)
        return self.min_depth

    def dfs(self, root: TreeNode, depth: int) -> None:
        if root.left is None and root.right is None:
            self.min_depth = min(self.min_depth, depth)

        if root.left is not None:
            self.dfs(root.left, depth + 1)

        if root.right is not None:
            self.dfs(root.right, depth + 1)
