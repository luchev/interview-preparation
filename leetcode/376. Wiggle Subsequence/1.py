# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        longest_wiggle = 1
        sequence_is_increasing = None
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if sequence_is_increasing != True:
                    longest_wiggle += 1
                sequence_is_increasing = True
            if nums[i - 1] > nums[i]:
                if sequence_is_increasing != False:
                    longest_wiggle += 1
                sequence_is_increasing = False

        return longest_wiggle
