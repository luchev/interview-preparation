# Complexity (n = number of vertices, k = number of edges)
# Time complexity: O(n + k)
# Space complexity: O(n + k)

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph, edges = createGraph(n, connections)
        ranks = [None] * n
        dfs(graph, edges, ranks, 0, 0)
        return edges
        
def dfs(graph, edges, ranks, root, current_rank):
    if ranks[root] is not None:
        return ranks[root]
    
    ranks[root] = current_rank
    min_rank = current_rank + 1
    for neigh in graph[root]:
        if ranks[neigh] == current_rank - 1: # skip parrent
            continue
        
        neigh_rank = dfs(graph, edges, ranks, neigh, current_rank + 1)
        if neigh_rank <= current_rank:
            edges.remove((min(root, neigh), max(root,neigh)))
        
        min_rank = min(min_rank, neigh_rank)
    
    return min_rank

def createGraph(n: int, connections: List[List[int]]):
    graph = defaultdict(list)
    edges = set()        
    for x,y in connections:
        graph[x].append(y)
        graph[y].append(x)
        edges.add((min(x,y), max(x,y)))

    return graph, edges
