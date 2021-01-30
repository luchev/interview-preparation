# Complexity (n = number of items in the list, m = max(nums))
# Time complexity: O(n * log(n) * log(m))
# Space complexity: O(n)

import math
import heapq
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maximums = []
        for x in nums:
            if x % 2 == 0:
                maximums.append(-x)
            else:
                maximums.append(-x * 2)
        minimum = -max(maximums)
        
        heapq.heapify(maximums)
        min_deviation = math.inf
        while maximums:
            top = -heapq.heappop(maximums)
            min_deviation = min(min_deviation, top - minimum)
            if top % 2 == 0:
                minimum = min(minimum, top // 2)
                heapq.heappush(maximums, -top // 2)
            else:
                break
        return min_deviation
