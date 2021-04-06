# Complexity ()
# Time complexity: O(1)
# Space complexity: O(1)

from typing import List

class Solution:
    def minOperations(self, n: int) -> int:
        half = n // 2
        if n & ~1 == n:
            return n * (n + 1) // 2 - (half * (half+1))
        else:
            return (half * (half+1))

# 1 3 5 7
# n // 2 + 1 + 3 + 5 + ... + n // 2
# 1 3 5 7 9
# 2 + 4 + ... + n // 2
