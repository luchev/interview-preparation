# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        subarrs = 0
        left = 0
        right = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left < right:
                product /= nums[left]
                left += 1
            if product < k:
                subarrs += right - left + 1

        return subarrs
