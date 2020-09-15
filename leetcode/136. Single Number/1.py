# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

import functools

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x ^ y, nums)
