# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replaceIndex = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[replaceIndex] = nums[index]
                replaceIndex += 1
        return replaceIndex
