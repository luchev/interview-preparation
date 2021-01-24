# Complexity (n = length of s = length of t)) 
# If the length is different with more than 2, the time complexity is O(1)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        
        if len(s) == len(t) - 1:
            left = 0
            right = 0
            changes = 0
            while left < len(s) and right < len(t):
                if s[left] != t[right]:
                    right += 1
                    changes += 1
                    continue
                left += 1
                right += 1
            return changes <= 1
        elif len(s) == len(t):
            changes = 0
            for x,y in zip(s, t):
                if x != y:
                    changes += 1
            return changes == 1
        else:
            return False
