# Doesn't pass the time limit tests
# Complexity (n = numbers in he input list)
# Time complexity: O(2^n)
# Space complexity: O(n) for the recursion

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total >> 1 << 1 != total:
            return False
        half = total // 2
        if max(nums) > half:
            return False
        return recursiveSubsetSum(nums, 0, half)


def recursiveSubsetSum(nums, i, remaining_sum):
    if remaining_sum == 0:
        return True
    if i == len(nums):
        return False
    return recursiveSubsetSum(nums, i+1, remaining_sum - nums[i]) or recursiveSubsetSum(nums, i+1, remaining_sum)
