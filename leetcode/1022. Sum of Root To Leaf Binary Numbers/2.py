# Complexity (n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0

        total = 0
        nodeStack = [(root, 0)]
        while len(nodeStack) != 0:
            node, currentNumber = nodeStack.pop()

            if node is not None:
                currentNumber = (currentNumber << 1) | node.val
                if node.left is None and node.right is None:
                    total += currentNumber
                else:
                    nodeStack.append((node.left, currentNumber))
                    nodeStack.append((node.right, currentNumber))

        return total
