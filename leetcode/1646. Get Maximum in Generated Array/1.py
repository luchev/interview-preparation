# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        nums = [0, 1] + [0] * n
        for i in range(2, n+1):
            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2 + 1]
        return max(nums)
