# Complexity (n = number of nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        result = defaultdict(list)
        def dfs(root, layer):
            if not root:
                return layer
            layer = max(dfs(root.left, layer), dfs(root.right, layer))
            result[layer].append(root.val)
            return layer + 1
        dfs(root, 0)
        return result.values()