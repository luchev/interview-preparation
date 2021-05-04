# Complexity (n = length of input array)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        bi = None
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if bi is not None:
                    return False
                bi = i
                
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                
        return True