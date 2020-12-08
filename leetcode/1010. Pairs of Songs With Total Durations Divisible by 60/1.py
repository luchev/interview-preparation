# Complexity (n = number of numbers in the list)
# Time complexity: O(n)
# Space complexity: O(1) because we have a constant 60-sized array

from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = [0] * 60
        pairs = 0
        for x in time:
            pairs += counter[(60 -(x % 60)) % 60]
            counter[x % 60] += 1
        return pairs
