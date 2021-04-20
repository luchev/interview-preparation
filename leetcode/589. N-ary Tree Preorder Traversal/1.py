# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def dfs(root: 'Node'):
            if root is None:
                return
            result.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return result
