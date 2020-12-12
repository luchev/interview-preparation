# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        max_depth = dfs(root, 0)
        while root.left_depth != root.right_depth:
            if root.left_depth > root.right_depth:
                root = root.left
            else:
                root = root.right
        return root


def dfs(root: TreeNode, current_depth: int) -> int:
    if not root:
        return current_depth
    root.left_depth = dfs(root.left, current_depth + 1)
    root.right_depth = dfs(root.right, current_depth + 1)
    return max(root.left_depth, root.right_depth)
