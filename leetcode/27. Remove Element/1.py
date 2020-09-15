# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swapIndex = len(nums) - 1
        i = 0
        while i <= swapIndex:
            if nums[i] == val:
                nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
                swapIndex -= 1
            else:
                i += 1
        return i
