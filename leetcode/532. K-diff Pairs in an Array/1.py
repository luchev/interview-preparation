# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
import collections

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = collections.Counter(nums)
        if k == 0:
            return len([k for key in counts if counts[key] >= 2])
        return len([k for key in counts if (key - k) in counts])
