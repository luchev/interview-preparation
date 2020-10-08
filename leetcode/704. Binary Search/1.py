# Complexity (n = number of items in nums)
# Time complexity: O(log(n))
# Space complexity: O(1)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bst(nums, target, 0, len(nums) - 1)

    def bst(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.bst(nums, target, mid + 1, right)
        else:
            return self.bst(nums, target, left, mid - 1)
