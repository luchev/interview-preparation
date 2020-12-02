# Complexity (n = nodes in the tree, h = height of the tree)
# Time complexity: O(n)
# Space complexity: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0
        self.dfs_node_sum(root)
        return self.tilt

    def dfs_node_sum(self, root: TreeNode):
        if root is None:
            return 0
        left = self.dfs_node_sum(root.left)
        right = self.dfs_node_sum(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val
