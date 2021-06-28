# Complexity (n = number of edges, k = number of vertices)
# Time complexity: O(n + k)
# Space complexity: O(n + k)

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
        
        return dfs(graph, source, destination, [None] * n)

def dfs(graph, source, destination, visited):
    if visited[source] == 'c':
        return True
    if visited[source] == 'o':
        return False
    
    if len(graph[source]) == 0:
        return source == destination
    
    visited[source] = 'o'
    for neighbour in graph[source]:
            if not dfs(graph, neighbour, destination, visited):
                return False
    visited[source] = 'c'
    return True