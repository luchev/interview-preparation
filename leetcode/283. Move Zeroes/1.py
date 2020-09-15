# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapIndex = 0
        while swapIndex < len(nums) and nums[swapIndex] != 0:
            swapIndex += 1

        for i in range(swapIndex + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
                swapIndex += 1
