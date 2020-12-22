# Complexity (n = nodes in tree)
# Time complexity: O(n)
# Space complexity: O(n)

from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findNearestRightNode(self, root: TreeNode, target: TreeNode) -> TreeNode:
        current_frontier = Queue()
        next_frontier = Queue()

        if root:
            current_frontier.put(root)

        target_hit = False
        while current_frontier.qsize() > 0:
            current_vertex = current_frontier.get()

            if target_hit:
                return current_vertex
            if current_vertex.val == target.val:
                if current_frontier.qsize() == 0:
                    return None
                target_hit = True

            if current_vertex.left:
                next_frontier.put(current_vertex.left)
            if current_vertex.right:
                next_frontier.put(current_vertex.right)

            if current_frontier.qsize() == 0:
                current_frontier = next_frontier
                next_frontier = Queue()

        return None
