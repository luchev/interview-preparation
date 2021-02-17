# Complexity (n = length of input array)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxVolume = 0
        
        while left < right:
            maxVolume = max(maxVolume, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxVolume
