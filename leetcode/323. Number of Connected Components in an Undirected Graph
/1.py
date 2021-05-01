# Complexity (n = vertices, k = edges)
# Time complexity: O(n + k)
# Space complexity: O(n)

from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        visited = [False] * n
        components = 0
        for i in range(n):
            if visited[i] == False:
                components += 1
                dfs(graph, i, visited)
        
        return components

def dfs(graph, root, visited):
    if visited[root]:
        return
    
    visited[root] = True
    for child in graph[root]:
        dfs(graph, child, visited)