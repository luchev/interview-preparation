# Complexity (n = numbers in he input list, m = sum of all numbers / 2)
# Time complexity: O(n * m)
# Space complexity: O(n * m)

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total >> 1 << 1 != total:
            return False
        half = total // 2
        if max(nums) > half:
            return False

        dp = [[False] * (half+1) for _ in range(len(nums) + 1)]
        for row in range(len(dp)):
            dp[row][0] = True

        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])):
                x = nums[row - 1]
                dp[row][col] = dp[row - 1][col]
                if col - x >= 0:
                    dp[row][col] |= dp[row - 1][col - x]

        return dp[-1][-1]
