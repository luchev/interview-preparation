# Complexity (n = word1 length, k = word2 length)
# Time complexity: O(n * k)
# Space complexity: O(n * k)

from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
      return len(word1) + len(word2) - 2 * lcs(word1, word2, len(word1), len(word2))

@cache        
def lcs(a, b, ai, bi):
    if ai == 0 or bi == 0:
        return 0
    if a[ai - 1] == b[bi - 1]:
        return 1 + lcs(a, b, ai - 1, bi - 1)
    else:
        return max(lcs(a, b, ai - 1, bi), lcs(a, b, ai, bi - 1))