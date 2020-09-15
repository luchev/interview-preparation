# Complexity(n = input string length)
# Time complexity: O(n)
# Space complexity: O(ALPHABET_SIZE)

import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = collections.Counter(s)
        for index,char in enumerate(s):
            if chars[char] == 1:
                return index
        return -1
