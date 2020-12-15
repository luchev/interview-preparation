# Complexity (n = numbers in nums)
# Time complexity: O(n)
# Space complexity: O(1) excluding the output array

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        out = []
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                out.append(nums[left] ** 2)
                left += 1
            else:
                out.append(nums[right] ** 2)
                right -= 1
        return reversed(out)
