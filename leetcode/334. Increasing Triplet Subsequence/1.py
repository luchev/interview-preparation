# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List
import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = math.inf
        mid = math.inf
        for x in nums:
            if x < left:
                left = x
            elif left < x < mid:
                mid = x
            elif mid != math.inf and mid < x:
                return True
        return False
