# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n) for the recursion stack

from typing import Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(dfs(root))

def dfs(root: TreeNode) -> Tuple[int, int]:
    if not root:
        return 0, 0

    left_with, left_without = dfs(root.left)
    right_with, right_without = dfs(root.right)

    with_current = root.val + left_without + right_without
    without_current = max(left_with, left_without) + max(right_with, right_without)

    return with_current, without_current
