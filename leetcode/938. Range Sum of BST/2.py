# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n) for the recursion stack

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.range_sum = 0
        self.dfs(root, low, high)
        return self.range_sum

    def dfs(self, root, low, high):
        if not root:
            return
        if low <= root.val <= high:
            self.range_sum += root.val
            self.dfs(root.left, low, high)
            self.dfs(root.right, low, high)
        if root.val < low:
            self.dfs(root.right, low, high)
        if high < root.val:
            self.dfs(root.left, low, high)
