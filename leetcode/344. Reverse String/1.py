# Complexity(n = input string length)
# Time complexity: O(n)
# Space complexity: O(1)

import math
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, math.floor(len(s) / 2)):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
