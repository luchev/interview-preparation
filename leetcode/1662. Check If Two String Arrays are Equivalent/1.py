# Complexity (n = characters in word1, m = characters in word2)
# Time complexity: O(min(m. n))
# Space complexity: O(1)

from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for a,b in zip(itr(word1), itr(word2)):
            if a != b:
                return False
        return True
        
def itr(arr: List[str]):
    for word in arr:
        for char in word:
            yield char
    yield None
