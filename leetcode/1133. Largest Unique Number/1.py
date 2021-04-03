# Complexity (n = length of input array)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List
from collections import Counter

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        return max([-1] + [ x for x,count in Counter(A).items() if count == 1 ])
