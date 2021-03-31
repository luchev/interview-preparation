# Complexity (n = courses, k = number of relations)
# Time complexity: O(n + k)
# Space complexity: O(n + k)

from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        tree = defaultdict(list)
        for parent, child in relations:
            tree[parent].append(child)
        
        visited = ['u'] * (n + 1) # Unvisited Visited and Open
        height = [0] * (n + 1)
        def dfs(vertex):
            if visited[vertex] == 'v':
                return height[vertex]
            if visited[vertex] == 'o':
                return math.inf
            
            visited[vertex] = 'o'
            if len(tree[vertex]) > 0:
                vHeight = max(dfs(child) for child in tree[vertex])
            else:
                vHeight = 0
            visited[vertex] = 'v'
            
            height[vertex] = vHeight + 1
            return vHeight + 1
        
        for x in range(1, n + 1):
            dfs(x)

        semesters = max(height)
        if semesters != math.inf:
            return semesters
        return -1
