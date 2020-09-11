# Complexity (n = nodes in the list, h = height of the tree)
# Time complexity for next: Amortized O(1)
# Time complexity for hasNext: O(1)
# Time complexity for full iteration: O(n)
# Space complexity: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self._go_left(self.root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if len(self.stack) > 0:
            next_node = self.stack.pop()
            self._go_left(next_node.right)
            return next_node.val
        else:
            return None

    def _go_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
