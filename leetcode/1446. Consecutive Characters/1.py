# Complexity (n = length of string)
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        char = None
        curr_count = 0
        max_count = 0
        for c in s:
            if c != char:
                char = c
                max_count = max(max_count, curr_count)
                curr_count = 1
            else:
                curr_count += 1
        return max(max_count, curr_count)
