# Complexity n = length of t
# Time complexity O(n)
# Space complexity O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        for char in t:
            if s_pointer < len(s) and s[s_pointer] == char:
                s_pointer += 1
        return s_pointer == len(s)

