# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        l = 1
        for i in range(1, len(nums)):
            l *= nums[i - 1]
            result[i] = l

        r = 1
        for i in range(len(nums) - 2, -1, -1):
            r *= nums[i + 1]
            result[i] *= r

        return result
