# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k in [0, 1]:
            return 0
        nums = [1] + nums
        left = 0
        cur_mul = 1
        result = 0
        for right in range(len(nums)):
            cur_mul *= nums[right]
            while cur_mul >= k:
                left += 1
                cur_mul /= nums[left]
            result += right - left
        return result
