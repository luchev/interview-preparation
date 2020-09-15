# Complexity (n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n) on the stack

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else:
                rightLeftMost = root.right
                while rightLeftMost.left is not None:
                    rightLeftMost = rightLeftMost.left
                root.val = rightLeftMost.val
                root.right = self.deleteNode(root.right, rightLeftMost.val)
                print(root.val)
        return root
