# Complexity (n = nodes in tree, h = height of tree)
# Time complexity: O(n)
# Space complexity: O(h)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return dfs(cloned, target.val)
        
def dfs(root: TreeNode, target: int):
    if not root:
        return None
    if root.val == target:
        return root
    left = dfs(root.left, target)
    if left:
        return left
    return dfs(root.right, target)
