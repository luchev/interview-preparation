# Complexity (n = nodes in the tree)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        if len(edges) == 1:
            return [0,1]

        graph = [set() for i in range(n)]
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)

        leaves = []
        for index, neighbours in enumerate(graph):
            if len(neighbours) == 1:
                leaves.append(index)

        while leaves:
            next_level = []

            for leaf in leaves:
                for neigh in graph[leaf]:
                    graph[neigh].remove(leaf)
                    if len(graph[neigh]) == 1:
                        next_level.append(neigh)
            if next_level:
                leaves = next_level
            else:
                break
        return leaves
