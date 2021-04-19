# Complexity (n = length of nums, t = target)
# Time complexity: O(n * t)
# Space complexity: O(t)

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        targets = [0] * (target + 1)
        
        targets[0] = 1
        for i in range(1, len(targets)):
            for x in nums:
                if i >= x:
                    targets[i] += targets[i - x]
        return targets[-1]