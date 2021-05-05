# Complexity (n = input array size)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currentEnd = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
        return jumps