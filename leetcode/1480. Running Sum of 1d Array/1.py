# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        running_sum = [nums[0]]
        for i in range(1, len(nums)):
            running_sum.append(running_sum[-1] + nums[i])
        return running_sum
