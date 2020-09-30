# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n) because we modify the input

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                else:
                    break
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1
