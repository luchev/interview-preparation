# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(ALPABET_SIZE)

import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        letterBank = collections.Counter(magazine)
        for char in ransomNote:
            if char not in letterBank:
                return False
            letterBank[char] -= 1
            if letterBank[char] < 0:
                return False

        return True
