# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(1)

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        leftmost = root
        while leftmost:
            curr = leftmost
            while curr and curr.left:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            leftmost = leftmost.left

        return root
