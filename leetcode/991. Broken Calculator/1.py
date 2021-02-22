# Complexity (n = Y)
# Time complexity: O(log(n))
# Space complexity: O(1)

from typing import List

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ops = 0
        while Y > X:
            ops += 1
            if Y % 2 == 0:
                Y /= 2
            else:
                Y += 1
        return int(ops + X - Y)
