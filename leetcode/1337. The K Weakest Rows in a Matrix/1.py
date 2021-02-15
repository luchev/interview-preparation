# Complexity (n = matrix rows, m = matrix cols, k = desired number of rows)
# Time complexity: O(n * m + n * log(k))
# Space complexity: O(n)

from typing import List
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = [(sum(x), i) for i,x in enumerate(mat)]
        heapq.heapify(rows)
        result = []
        for i in range(k):
            result.append(heapq.heappop(rows)[1])
        return result
