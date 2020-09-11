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
        self.iter = self.iterate(root)
        self.advance()

    def next(self) -> int:
        """
        @return the next smallest number
        """
        current_node = self.current_node
        self.advance()
        return current_node.val

    def iterate(self, root):
        if root is None:
            return
        for x in self.iterate(root.left):
            yield x

        yield root

        for x in self.iterate(root.right):
            yield x

    def advance(self):
        try:
            self.current_node = next(self.iter)
        except:
            self.current_node = None

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.current_node is not None
