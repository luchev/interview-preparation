# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n) for the recursion stack

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        
        total = 0
        if L <= root.val <= R:
            total += root.val

        return total + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
