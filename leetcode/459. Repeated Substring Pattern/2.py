# Complexity (n = string length)
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
