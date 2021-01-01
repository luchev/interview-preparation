# Complexity (n = string length)
# Time complexity: O(n)
# Space complexity: O(alphabet size)

from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        one_odd = False
        for _,count in counter.items():
            if count % 2 == 1 and one_odd:
                return False
            elif count % 2 == 1:
                one_odd = True
        return True
