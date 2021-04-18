# Complexity (n = input string length)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('\W+|_', '', s).lower()
        return s == s[::-1]
