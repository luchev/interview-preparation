# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_simple(nums[1:]), self.rob_simple(nums[:-1]))

    def rob_simple(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        total = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            total.append(max(total[-1], total[-2] + nums[i]))
        return total[-1]
