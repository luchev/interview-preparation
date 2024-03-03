# Complexity (n = len(word1), m = len(word2))
# Time complexity: O(n * m)
# Space complexity: O(n * m)

from functools import cache
class Solution:
    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "" and word2 == "":
            return 0
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        return 1 + min(
            self.minDistance(word1[1:], word2[1:]),
            self.minDistance(word1[1:], word2),
            self.minDistance(word1, word2[1:]),
        )
