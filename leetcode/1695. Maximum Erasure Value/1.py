# Complexity (n = input array size)
# Time complexity: O(n) per operation
# Space complexity: O(n)

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        window = set()
        currentSum = 0
        bestSum = 0
        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                currentSum -= nums[left]
                left += 1
            window.add(nums[right])
            currentSum += nums[right]
            bestSum = max(bestSum, currentSum)
            
        return bestSum