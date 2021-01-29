# Complexity (n = number of nodes in the tree, k = width of tree)
# Time complexity: O(n * log(n/k))
# Space complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        tree = defaultdict(list)
        min_x = 1
        max_x = -2
        def dfs(root, x, y):
            if root:
                nonlocal min_x
                nonlocal max_x
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                
                tree[x].append((y, root))
                dfs(root.left, x - 1, y + 1)
                dfs(root.right, x + 1, y + 1)
        
        dfs(root, 0, 0)
        for x in range(min_x, max_x + 1):
            tree[x].sort(key=lambda x: (x[0], x[1].val))
            tree[x] = [x[1].val for x in tree[x]]
        
        return [tree[x] for x in range(min_x, max_x + 1)]
