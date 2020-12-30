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
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        hist = [0] * 10
        return dfs(root, hist)


def dfs(root: TreeNode, path: List[int]):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        oneOdd = False
        path[root.val] += 1
        for x in path:
            if x % 2 == 1:
                if not oneOdd:
                    oneOdd = True
                else:
                    path[root.val] -= 1
                    return 0
        path[root.val] -= 1
        return 1

    path[root.val] += 1
    palindromes = dfs(root.left, path) + dfs(root.right, path)
    path[root.val] -= 1

    return palindromes
