# Complexity(n = input string length)
# Time complexity: O(n)
# Space complexity: O(n)

import collections
import re
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        letterCounters = collections.Counter(s)
        if min([letterCounters[x] for x in letterCounters]) >= k:
            return len(s)

        charsFewerThanK = ''.join(
            [x if letterCounters[x] >= k else '' for x in letterCounters])
        if len(charsFewerThanK) == 0:
            return 0

        charsFewerThanKRegex = '[{}]+'.format(charsFewerThanK)
        potentialStrings = re.findall(charsFewerThanKRegex, s)

        return max([self.longestSubstring(x, k) for x in potentialStrings])
