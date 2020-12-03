# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        newHead = TreeNode()
        ptrNode = newHead

        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            top = stack.pop()
            ptrNode.right = TreeNode(top.val)
            ptrNode = ptrNode.right
            if top.right:
                stack.append(top.right)
                top = top.right
                while top.left:
                    stack.append(top.left)
                    top = top.left

        return newHead.right
