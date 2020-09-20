# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapIndex = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[swapIndex] = nums[i]
            swapIndex += 1

        for i in range(swapIndex, len(nums)):
            nums[i] = 0
