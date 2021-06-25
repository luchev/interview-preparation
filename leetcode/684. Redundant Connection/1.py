# Complexity (n = number of edges)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for index, (u,v) in enumerate(edges):
            graph[u].append((v, index)) # index = priority
            graph[v].append((u, index))
        
        seen = set()
        loopNode = None
        priority = -1
        def dfs(root, parent):
            nonlocal loopNode
            nonlocal priority
            if root in seen:
                loopNode = root
                return True, -1
            seen.add(root)
            for neighbour, index in graph[root]:
                if neighbour != parent:
                    isLoop, nextPriority = dfs(neighbour, root)
                    if isLoop:
                        priority = max(priority, index, nextPriority)
                        return not loopNode == root, priority
            return False, -1
        
        dfs(1, -1)
        return edges[priority]