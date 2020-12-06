# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

from queue import Queue

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        que = Queue()
        que.put(root)
        que.put(None)
        traversal_over = False
        prev_node = None
        while que.qsize() > 0:
            current = que.get()

            # Handle what level are we on
            if current is None and traversal_over:
                break
            elif current is None:
                traversal_over = True
                prev_node = None
                que.put(None)
                continue
            
            # Add children to queue
            traversal_over = False
            if current.left:
                que.put(current.left)
            if current.right:
                que.put(current.right)
            
            # Handle next pointer
            if current.left and current.right:
                current.left.next = current.right
                if prev_node:
                    prev_node.next = current.left
                prev_node = current.right
            elif current.left:
                if prev_node:
                    prev_node.next = current.left
                prev_node = current.left
            elif current.right:
                if prev_node:
                    prev_node.next = current.right
                prev_node = current.right
                
        return root
