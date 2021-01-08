# Complexity (n = length of tree (nodes in tree))
# Time complexity: O(n)
# Space complexity: O(1)

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        root_val = 0
        for node in tree:
            root_val ^= node.val
            for child in node.children:
                root_val ^= child.val
                
        for node in tree:
            if node.val == root_val:
                return node
        return None
