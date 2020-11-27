# Complexity (n = numbers in he input list, m = sum of all numbers / 2)
# Time complexity: O(n * m)
# Space complexity: O(m)

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total >> 1 << 1 != total:
            return False
        half = total // 2
        if max(nums) > half:
            return False

        sums = [False] * (half+1)
        sums[0] = True

        for row in range(1, len(nums) + 1):
            for col in reversed(range(nums[row - 1], half + 1)):
                sums[col] |= sums[col - nums[row - 1]]

        return sums[-1]
