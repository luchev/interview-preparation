# Complexity (n = number of nodes in the tree, h = height of the tree)
# Time complexity: O(h)
# Space complexity: O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node: Node) -> Node:
        nextNode = None

        if node.right is not None:
            nextNode = node.right
            while nextNode.left is not None:
                nextNode = nextNode.left
        else:
            while True:
                if node.parent is None:
                    return None

                if node.parent.left == node:
                    return node.parent
                else:
                    node = node.parent

        return nextNode
