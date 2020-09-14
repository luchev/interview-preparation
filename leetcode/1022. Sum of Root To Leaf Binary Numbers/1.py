# Complexity (n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n) or the height of the tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.sumLeaves(root, 0)

    def sumLeaves(self, root: TreeNode, currentNumber: int) -> int:
        if root is None:
            return 0

        currentNumber = (currentNumber << 1) | root.val

        if root.left is None and root.right is None:
            return currentNumber
        else:
            return self.sumLeaves(root.left, currentNumber) + self.sumLeaves(root.right, currentNumber)
