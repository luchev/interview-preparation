# Complexity (n = number of instructions)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

from typing import List
from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sorted_list = SortedList()
        mod = 10 ** 9 + 7
        
        total = 0
        
        for index, val in enumerate(instructions):
            left = sorted_list.bisect_left(val)
            right = index - sorted_list.bisect_right(val)
            total += min(left, right)
            sorted_list.add(val)
        return total % mod
