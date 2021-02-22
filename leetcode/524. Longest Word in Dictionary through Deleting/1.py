# Complexity (n = length of s, k = number of items in d)
# Time complexity: O(n * k)
# Space complexity: O(n)

from typing import List

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isSubsequence(short, long):
            itr = iter(long)
            return all(c in itr for c in short)
        best = ''
        for word in d:
            if isSubsequence(word, s) and (-len(word), word) < (-len(best), best):
                best = word
        return best
