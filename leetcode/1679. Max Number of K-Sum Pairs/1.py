# Complexity (n = numbers in nums)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        available = defaultdict(int)
        pairs = 0
        for x in nums:
            if available[k - x] > 0:
                available[k - x] -= 1
                pairs += 1
            else:
                available[x] += 1
        return pairs
