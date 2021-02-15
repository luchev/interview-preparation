# Complexity (n = matrix rows, m = matrix cols, k = desired number of rows)
# Time complexity: O(n * log(m) + n * log(k))
# Space complexity: O(n)

from typing import List
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = [(findLastOne(x), i) for i,x in enumerate(mat)]
        heapq.heapify(rows)
        result = []
        for i in range(k):
            result.append(heapq.heappop(rows)[1])
        return result
    
def findLastOne(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1
    rightMostOne = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == 1:
            rightMostOne = mid
            left = mid + 1
        else:
            right = mid - 1
    return rightMostOne + 1
