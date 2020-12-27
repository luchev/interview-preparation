# Complexity (n = elements in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0

        graph = defaultdict(list)
        for i in range(len(arr)):
            graph[arr[i]].append(i)
        
        frontier = [0]
        level = 0
        visited = set()
        visited.add(0)
        while frontier:
            next_frontier = []
            
            for node in frontier:
                if node == len(arr) - 1:
                    return level
                
                for child in graph[arr[node]]:
                    if child not in visited:
                        next_frontier.append(child)
                        visited.add(child)
                        
                del graph[arr[node]]
                
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        next_frontier.append(child)
                        visited.add(child)
                        
            frontier = next_frontier
            level += 1
            
        return -1
