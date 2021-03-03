# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = len(nums) * (len(nums) + 1) // 2
        return expectedSum - sum(nums)
