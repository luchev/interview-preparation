# Complexity (n = input array size)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        result = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            new = heapq.heappop(sticks) + heapq.heappop(sticks)
            result += new
            heapq.heappush(sticks, new)
            
        return result