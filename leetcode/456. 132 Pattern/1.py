# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
import math

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k = -math.inf
        js = []
        for x in reversed(nums):
            if x < k:
                return True
            else:
                while len(js) > 0 and js[-1] < x:
                    k = js.pop()
            js.append(x)
        return False
