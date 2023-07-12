# Complexity (n = graph nodes, m = graph connections)
# Time complexity: O(n * m)
# Space complexity: O(n)

from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        states = defaultdict(str)
        def dfs(current):
            if states[current] == 'closed':
                return 'closed'
            if states[current] == 'loop' or states[current] == 'open':
                return 'loop'
            if states[current] == '':
                states[current] = 'open'
            for child in graph[current]:
                res = dfs(child)
                if res == 'loop':
                    states[current] = 'loop'
            if states[current] == 'loop':
                return 'loop'
            states[current] = 'closed'
            return 'closed'
        for start in range(len(graph)):
            dfs(start)
        
        result = []
        for i in range(len(graph)):
            if states[i] == 'closed':
                result.append(i)
        return result
