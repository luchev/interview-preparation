# Complexity (n = nums length)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        result = 0
        currentFlipped = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                currentFlipped += 1
                if currentFlipped > k:
                    while nums[left] == 1:
                        left += 1
                    left += 1
                    currentFlipped -= 1
            result = max(result, right - left + 1)
        return result