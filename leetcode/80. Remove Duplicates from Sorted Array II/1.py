# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        oneBehind = nums[0] + 1 # random different number
        twoBehind = nums[0] + 2 # random different number
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != twoBehind:
                nums[slow] = nums[fast]
                slow += 1
            twoBehind = oneBehind
            oneBehind = nums[fast]
        return slow
