# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return dfs(root)


def dfs(root: TreeNode) -> int:
    if not root:
        return 0
    return max(dfs(root.left) + 1, dfs(root.right) + 1)
