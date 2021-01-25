# Complexity (n = number of items in the array)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = k + 1
        for x in nums:
            if x == 0:
                dist += 1
            elif x == 1 and dist >= k:
                dist = 0
            else:
                return False
        return True
