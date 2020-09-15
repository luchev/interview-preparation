# Complexity (n = string length)
# Time complexity: O(n^2)
# Space complexity: O(1)

import math

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, math.floor(len(s) / 2) + 1):
            if len(s) % i == 0:
                possibleRepeat = True
                for j in range(i, len(s)):
                    if s[j % i] != s[j]:
                        possibleRepeat = False
                        break
                if possibleRepeat:
                    return True
        return False
