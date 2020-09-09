# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

import collections

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(collections.Counter(nums)) != len(nums)
