# Complexity (n = number of nodes, m = number of connections)
# Time complexity: O(n + m)
# Space complexity: O(n)

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for child, parent in prerequisites:
            graph[parent].append(child)

        def dfs(current):
            if states[current] == 'loop' or states[current] == 'open':
                return 'loop'
            if states[current] == 'closed':
                return 'closed'
            states[current] = 'open'
            for child in graph[current]:
                res = dfs(child)
                if res == 'loop':
                    return 'loop'
            states[current] = 'closed'
            return 'closed'
        
        states = defaultdict(str)
        for start in range(numCourses):
            dfs(start)
        print(states)
        return 'open' not in states.values()
