# Complexity (n = nodes in the tree, h = height)
# Time complexity: O(n)
# Space complexity: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_diff = 0
        self.dfs(root)
        return self.max_diff

    def dfs(self, root: TreeNode):
        if root is None:
            return None, None

        min_val = root.val
        max_val = root.val
        left_min, left_max = self.dfs(root.left)
        if left_min is not None:
            min_val = min(min_val, left_min)
            max_val = max(max_val, left_max)

        right_min, right_max = self.dfs(root.right)
        if right_min is not None:
            min_val = min(min_val, right_min)
            max_val = max(max_val, right_max)

        self.max_diff = max(self.max_diff, abs(
            root.val - max_val), abs(root.val - min_val))
        return min_val, max_val
