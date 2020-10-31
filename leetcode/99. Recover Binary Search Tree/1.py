# Complexity (n = nodes in the tree, h = heiht of the tree)
# Time complexity: O(n)
# Space complexity: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stak = []
        x = None
        y = None
        prev = None
        
        while len(stak) > 0 or root:
            while root:
                stak.append(root)
                root = root.left
            root = stak.pop()
            
            if prev and prev.val > root.val:
                y = root
                if x is None:
                    x = prev
                else:
                    break
            
            prev = root
            root = root.right
        x.val, y.val = y.val, x.val
