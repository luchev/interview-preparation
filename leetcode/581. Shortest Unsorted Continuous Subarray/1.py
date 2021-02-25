# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n) # O(1) is possible

from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = len(nums) - 1
        right = 0
        
        stak = []
        for i in range(len(nums)):
            while stak and nums[stak[-1]] > nums[i]:
                left = min(left, stak.pop())
            stak.append(i)
        
        stak = []
        for i in reversed(range(len(nums))):
            while stak and nums[stak[-1]] < nums[i]:
                right = max(right, stak.pop())
            stak.append(i)
        
        if left < right:
            return right - left + 1
        return 0
