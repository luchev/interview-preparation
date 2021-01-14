# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        while left < len(nums) and x - nums[left] >= 0:
            x -= nums[left]
            left += 1

        min_ops = left if x == 0 else math.inf
        right = len(nums) - 1
        while left >= 0:
            while right >= left and x - nums[right] >= 0:
                x -= nums[right]
                right -= 1

            if x == 0:
                min_ops = min(min_ops, left + len(nums) - right - 1)

            left -= 1
            x += nums[left]

        if min_ops != math.inf:
            return min_ops
        else:
            return -1
