# Complexity (n = number of people, k = number of edges)
# Time complexity: O(n + m)
# Space complexity: O(n)

from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        edges = defaultdict(set)
        for edge in trust:
            edges[edge[0]].add(edge[1])

        potential_judge = None
        for i in range(1, N + 1):
            if i not in edges:
                if potential_judge is not None:
                    return -1
                potential_judge = i

        for i in range(1, N + 1):
            if i != potential_judge:
                if potential_judge not in edges[i]:
                    return -1

        return potential_judge

"""    
Approach 2:

                 N-1
etering [ 0 , 0 , 3 , 2 ]
leaving [ 2 , 2 , 0 , 1 ]
                  0
"""
