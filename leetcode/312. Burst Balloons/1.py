# Complexity (n = balloons in the list)
# Time complexity: O(n^3)
# Space complexity: O(n^2)

from typing import List
from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @cache
        def dp(left, right):
            if left + 1 == right:
                return 0
            return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left + 1, right))
    
        return dp(0, len(nums) - 1)
