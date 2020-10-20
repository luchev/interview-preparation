# Complexity (n = number nodes in the graph, m = number of edges in the graph)
# Time complexity: O(n + m)
# Space complexity: O(n)

from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return node

        nodes = {}
        node_queue = [node]
        processed = set()
        while len(node_queue) > 0:
            current = node_queue.pop()
            if current.val in processed:
                continue
            processed.add(current.val)

            if current.val not in nodes:
                nodes[current.val] = Node(node.val)

            for neighbor in current.neighbors:
                node_queue.append(neighbor)
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)
                nodes[neighbor.val].neighbors.append(nodes[current.val])

        return nodes[node.val]
